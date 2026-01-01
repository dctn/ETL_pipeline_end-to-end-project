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