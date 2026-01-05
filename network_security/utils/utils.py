import os
import pickle
import sys

import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from network_security.logging import logger
from network_security.exception_handling.exception import SecurityException
import yaml
import pandas as pd

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise SecurityException(e,sys)

def write_yaml_file(file_path:str, data:dict) -> None:
    try:
        with open(file_path, 'w') as f:
            yaml.dump(data, f)
    except Exception as e:
        raise SecurityException(e,sys)

def generate_schema_yaml(file_path:str):
    try:
        df = pd.read_csv(file_path)

        all_columns_schema = {
            "columns": {col: str(dtype) for col, dtype in df.dtypes.items()}
        }

        numerical_columns_schema = {
            "numerical_columns": {col: str(dtype) for col, dtype in df.dtypes.items() if dtype == "int64"}
        }

        with open("data_schema/schema.yaml", "w") as f:
            yaml.dump(all_columns_schema,f, indent=4,default_flow_style=False,sort_keys=False)
            yaml.dump(numerical_columns_schema, f, indent=4,default_flow_style=False,sort_keys=False)

    except Exception as e:
        raise SecurityException(e,sys)

def read_file_to_df(file_path:str)->pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise SecurityException(e,sys)


def save_file_as_np(file_path:str, array:np.ndarray)->None:
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)
        with open(file_path, 'wb') as f:
            np.save(f, array)

    except Exception as e:
        raise SecurityException(e,sys)

def load_np_arr_file(file_path:str)->np.ndarray:
    try:
        with open(file_path, 'rb') as f:
            return np.load(file_path)
    except Exception as e:
        raise SecurityException(e,sys)

def save_pkl_file(file_path:str, obj:object)->None:
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)

    except Exception as e:
        raise SecurityException(e,sys)


def load_pkl_file(file_path:str)->object:
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        raise SecurityException(e,sys)


def evalulate_models(models,params,x_train,y_train,x_test,y_test):
    try:
        report = {}

        for model_name,model in models.items():

            param = params[model_name]

            grid_search = GridSearchCV(estimator=model, param_grid=param)
            grid_search.fit(x_train, y_train)

            model.set_params(**grid_search.best_params_)
            model.fit(x_train, y_train)

            y_trian_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            X_train_score = r2_score(y_train, y_trian_pred)
            X_test_score = r2_score(y_test, y_test_pred)

            report.update({
                model_name: X_test_score,
            })

        return report
    except Exception as e:
        raise SecurityException(e,sys)




