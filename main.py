from configs import data_config, preprocessing_config, model_config
from marshmallow import Schema, fields, ValidationError
from src.collect_data import CollectData
from src.model import Model
from src.preprocessing import Preprocessing
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, request, jsonify
import pandas as pd
import sys
import os
from src.validation import RequestSchema
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

config = {
        'scaler_file': preprocessing_config.scaler_file,
        'processing_map': preprocessing_config.processing_map
}

app = Flask(__name__)

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

inputManager = CollectData(data_config)
preprocessing = Preprocessing(config)
modelManager = Model(model_config)

@app.errorhandler(ValidationError)
def handle_expected_exception(e):
    return jsonify(e.messages), 400

@app.route('/predict', methods=['POST'])
def getPredict():
    request_body = request.json
    schema = RequestSchema()
    try:
        result = schema.load(request_body)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Create DataFrame with correct column names
    dataset = pd.DataFrame({
            'Radius [cm]': [request_body['radius']],
            'Layers': [request_body['layers']],
            'Topping': [request_body['topping']]
    })
    
    process_dataset = preprocessing.process_data(dataset)
    prediction = modelManager.predict(process_dataset)
    
    # Convert numpy array to Python float
    prediction_value = float(prediction[0])
    
    return jsonify({
            "predict_result": prediction_value,
            "input_data": {
                    "radius": request_body['radius'],
                    "layers": request_body['layers'],
                    "topping": request_body['topping']
            }
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)