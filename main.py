from marshmallow import ValidationError
from src.collect_data import collect_data
from src.model import Model
from src.preprocessing import Preprocessing
from src.validation import RequestSchema
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

inputManager = CollectData(data_config)
preprocessing = Preprocessing(preprocessing_config)
modelManager = Model(model_config)
input_params = ['Radius [cm]', 'Layers', 'Topping']

@app.route('/predict', methods=['GET'])
def getPredict():