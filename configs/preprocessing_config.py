import os

label_encoder_file = os.getenv('label_encoder_file')
scaler_file = 'models/One Hot Encoder.pkl'

processing_map = {
        'topping_encoder'    : 'ohe_topping',  # OneHotEncoder for topping
        'numeric_columns'    : ['Radius [cm]', 'Layers'],  # Numeric features
        'categorical_columns': ['Topping'],  # Categorical features
        
        # Default values for missing data
        'radius_fillna'      : 17.5,  # Example mean value
        'layers_fillna'      : 2,  # Example mode value
        'topping_fillna'     : 'Simple',  # Example most common value
        
        # Scaling configuration
        'scaler_columns'     : ['Radius [cm]', 'Layers'],
        
        # Model parameters
        'test_size'          : 0.2,
        'random_state'       : 42
}