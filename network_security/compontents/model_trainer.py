from network_security.utils.estimator import NetworkModel
from network_security.utils.utils import *
from network_security.utils.ml_utlis import *
from network_security.entity.artifact_entity import ModelTrainerArtifact, DataTransformingArtifact
from network_security.entity.config_entity import ModelTrainingConfig
from network_security.exception_handling.exception import SecurityException
from network_security.logging.logger import logging

import pandas as pd
import numpy as np
import os,sys

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainingConfig, data_transforming_artifact: DataTransformingArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transforming_artifact = data_transforming_artifact
        except Exception as e:
            raise SecurityException(e,sys)


    def model_trainer(self,x_train,y_train,x_test,y_test):
        try:
            models = {
                'RandomForestClassifier': RandomForestClassifier(),
                'AdaBoostClassifier': AdaBoostClassifier(),
                'GradientBoostingClassifier': GradientBoostingClassifier(),
                'KNeighborsClassifier': KNeighborsClassifier(),
                'LogisticRegression': LogisticRegression(),
            }

            params = {
                "RandomForestClassifier": {
                    "n_estimators": [100],  # ⏱ large values are slow
                    "max_depth": [None, 20],
                    "min_samples_split": [2, 5],
                    "min_samples_leaf": [1],
                    # "bootstrap": [True, False],           # ❌ doubles search time
                },

                "AdaBoostClassifier": {
                    "n_estimators": [50, 100],  # ⏱ >200 is slow
                    "learning_rate": [0.1, 1.0],
                },

                "GradientBoostingClassifier": {
                    "n_estimators": [100],  # ⏱ 200+ slow
                    "learning_rate": [0.1],
                    "max_depth": [3],
                    # "subsample": [0.8, 1.0],               # ❌ increases combinations
                },

                "KNeighborsClassifier": {
                    "n_neighbors": [3, 5, 7],
                    "weights": ["uniform"],
                    # "metric": ["euclidean", "manhattan"], # ❌ costly distance calc
                },

                "LogisticRegression": {
                    "C": [0.1, 1],
                    "penalty": ["l2"],
                    "solver": ["lbfgs"],
                    "max_iter": [200],                   # ❌ rarely needed
                },
            }

            model_report:dict = evalulate_models(models,params,x_train,y_train,x_test,y_test)

            # get model with best score
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            #predict with best model
            y_train_pred = best_model.predict(x_train)
            y_test_pred = best_model.predict(x_test)

            best_model_train_metric = get_classification_report(y_train,y_train_pred)
            best_model_test_metric = get_classification_report(y_test,y_test_pred)

            # loading pre-processor object from artifact
            data_transform_preprocessor = load_pkl_file(self.data_transforming_artifact.transformation_object_file_path)

            dir_path = os.path.dirname(self.model_trainer_config.model_trained_file_path)
            os.makedirs(dir_path, exist_ok=True)

            network_model = NetworkModel(preprocessor=data_transform_preprocessor,model=best_model)
            save_pkl_file(self.model_trainer_config.model_trained_file_path, network_model)

            artifact = ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.model_trained_file_path,
                                            train_metrics_artifact=best_model_train_metric,test_metrics_artifact=best_model_test_metric)

            logging.info(f"Best Model: {best_model_name} info {artifact}")
            return artifact

        except Exception as e:
            raise SecurityException(e,sys)

    def initialize_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path = self.data_transforming_artifact.transformed_train_file_path
            test_file_path = self.data_transforming_artifact.transformed_test_file_path

            # loading np array file
            train_np = load_np_arr_file(train_file_path)
            test_np = load_np_arr_file(test_file_path)

            x_train,y_train = train_np[:,:-1],  train_np[:,-1]
            x_test,y_test = test_np[:,:-1], test_np[:,-1]

            model_trainer_artifact = self.model_trainer(x_train,y_train,x_test,y_test)

            return model_trainer_artifact

        except Exception as e:
            raise SecurityException(e,sys)