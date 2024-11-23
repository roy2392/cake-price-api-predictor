import pickle
from sklearn.preprocessing import OneHotEncoder

class Encoder():
    def __init__(self, config):
        self.model_path = config.model_path
        self.load_model()
    
    def load_model(self):
        with open(self.model_path, 'rb') as f:
            self.encoder = pickle.load(f)
    
    def transform(self, dataset):
        return self.encoder.transform(dataset)
    
    def fit_transform(self, dataset):
        return self.encoder.fit_transform(dataset)
