from src.exceptions import DependencyException
import pickle
import pandas as pd
from typing import Dict, Any

class Preprocessing:
    def __init__(self, config: Dict[str, Any]):
        self.scaler_file = config.get('scaler_file')
        self.processing_map = config.get('processing_map')
        self.scaler = None
        self.topping_encoder = None
    
    def load_dependency(self):
        try:
            with open(self.scaler_file, 'rb') as f:
                self.scaler = pickle.load(f)
            
            with open(self.processing_map['topping_encoder'], 'rb') as f:
                self.topping_encoder = pickle.load(f)
        
        except Exception as e:
            raise DependencyException(f'Preprocessing load_dependency failed: {str(e)}') from e
    
    def _processing_data(self, dataset: pd.DataFrame) -> pd.DataFrame:
        try:
            # Process numeric features
            numeric_features = dataset[self.processing_map['numeric_columns']].copy()
            scaled_features = self.scaler.transform(numeric_features)
            scaled_df = pd.DataFrame(
                    scaled_features,
                    columns=self.processing_map['numeric_columns'],
                    index=dataset.index
            )
            
            # Process categorical features
            categorical_features = dataset[self.processing_map['categorical_columns']].copy()
            topping_encoded = self.topping_encoder.transform(categorical_features)
            topping_df = pd.DataFrame(
                    topping_encoded,
                    columns=self.topping_encoder.get_feature_names_out(),
                    index=dataset.index
            )
            
            # Combine features
            return pd.concat([scaled_df, topping_df], axis=1)
        
        except Exception as e:
            raise DependencyException(f'Error in _processing_data: {str(e)}') from e
    
    def process_data(self, dataset: pd.DataFrame) -> pd.DataFrame:
        self.load_dependency()
        try:
            return self._processing_data(dataset)
        except Exception as e:
            raise DependencyException(f'Error processing data: {str(e)}') from e