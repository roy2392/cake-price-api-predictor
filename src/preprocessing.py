from src.exceptions import DependencyException
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pickle
import pandas as pd

class Preprocessing:
    def __init__(self, config):
        self.encoder_file = config.scaler_file
        self.scaler_file = config.scaler_file
        self.processing_map = config.processing_map
    
    def load_dependency(self):
        try:
            # Load OneHotEncoder for topping
            with open(self.encoder_file, 'rb') as f:
                self.topping_encoder = pickle.load(f)
            
            # Load StandardScaler for numeric features
            with open(self.scaler_file, 'rb') as f:
                self.scaler = pickle.load(f)
        
        except Exception as e:
            raise DependencyException('Preprocessing load_dependency failed') from e
    
    def _processing_data(self, dataset):
        # Handle missing values
        dataset['Radius [cm]'] = dataset['Radius [cm]'].fillna(
                self.processing_map['radius_fillna'])
        dataset['Layers'] = dataset['Layers'].fillna(
                self.processing_map['layers_fillna'])
        dataset['Topping'] = dataset['Topping'].fillna(
                self.processing_map['topping_fillna'])
        
        # One-hot encode the Topping column
        topping_encoded = self.topping_encoder.transform(
                dataset[['Topping']])
        topping_df = pd.DataFrame(
                topping_encoded,
                columns=self.topping_encoder.get_feature_names_out(),
                index=dataset.index
        )
        
        # Scale numeric features
        scaled_features = self.scaler.transform(
                dataset[self.processing_map['scaler_columns']])
        scaled_df = pd.DataFrame(
                scaled_features,
                columns=self.processing_map['scaler_columns'],
                index=dataset.index
        )
        
        # Combine all features
        processed_df = pd.concat([
                scaled_df,
                topping_df
        ], axis=1)
        
        # Optional feature engineering
        if self.processing_map.get('create_area', False):
            processed_df['Area'] = 3.14159 * dataset['Radius [cm]']**2
        
        if self.processing_map.get('create_volume', False):
            processed_df['Volume'] = processed_df['Area'] * dataset['Layers']
        
        return processed_df
    
    def processing_data(self, dataset):
        """Main processing method"""
        self.load_dependency()
        return self._processing_data(dataset)
    
    def fit_preprocessing(self, dataset):
        """Method to fit preprocessors during training"""
        try:
            # Fit StandardScaler
            self.scaler = StandardScaler()
            self.scaler.fit(dataset[self.processing_map['scaler_columns']])
            
            # Fit OneHotEncoder
            self.topping_encoder = OneHotEncoder(sparse_output=False)
            self.topping_encoder.fit(dataset[['Topping']])
            
            # Save fitted preprocessors
            with open(self.encoder_file, 'wb') as f:
                pickle.dump(self.topping_encoder, f)
            
            with open(self.scaler_file, 'wb') as f:
                pickle.dump(self.scaler, f)
        
        except Exception as e:
            raise DependencyException('Preprocessing fit_preprocessing failed') from e
