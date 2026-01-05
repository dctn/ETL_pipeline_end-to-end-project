from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    testing_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_file_report_path:str


@dataclass
class DataTransformingArtifact:
    transformed_train_file_path: str
    transformed_test_file_path: str
    transformation_object_file_path: str


@dataclass
class MetricsArtifact:
    f1_score: float
    recall: float
    precision: float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metrics_artifact:MetricsArtifact = MetricsArtifact
    test_metrics_artifact:MetricsArtifact = MetricsArtifact












