# configs/preprocessing_config.py
import os

# configs/preprocessing_config.py
processing_map = {
    'topping_encoder': 'models/OneHotEncoder.pkl',
    'numeric_columns': ['Radius [cm]', 'Layers'],
    'categorical_columns': ['Topping'],
    'radius_fillna': 17.5,
    'layers_fillna': 2,
    'topping_fillna': 'Simple',
    'scaler_columns': ['Radius [cm]', 'Layers'],
    'test_size': 0.2,
    'random_state': 42
}

scaler_file = 'models/Standard_Scaler.pkl'
