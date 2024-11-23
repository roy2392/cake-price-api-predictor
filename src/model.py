import pickle

class Model():
    def __init__(self, config):
        self.model_path = config.model_path
        self.load_model()
        
    def load_model(self):
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
            
    def predict(self, dataset):
        # TODO: add columns validation before predict
        return self.model.predict(dataset)