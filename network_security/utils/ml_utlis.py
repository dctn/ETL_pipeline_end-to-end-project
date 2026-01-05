import sys

from sklearn.metrics import f1_score, recall_score, precision_score

from network_security.entity.artifact_entity import MetricsArtifact
from network_security.exception_handling.exception import SecurityException

def get_classification_report(y_true, y_pred):
    try:
        f1 = f1_score(y_true, y_pred,)
        recall = recall_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)

        metric_artifact = MetricsArtifact(f1_score=f1, recall=recall, precision=precision)
        return metric_artifact
    except Exception as e:
        raise SecurityException(e,sys)