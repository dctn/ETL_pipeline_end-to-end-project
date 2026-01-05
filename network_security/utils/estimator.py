from network_security.exception_handling.exception import SecurityException
from network_security.logging.logger import logging

class NetworkModel:
    def __init__(self,preprocessor,model):
        self.preprocessor = preprocessor
        self.model = model

    def predict(self,x):
        preprocessed_x = self.preprocessor.preprocess(x)
        predicted_x = self.model.predict(preprocessed_x)
        return predicted_x