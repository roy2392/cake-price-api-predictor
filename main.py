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

@app.route('/predict', methods=['POST'])
def getPredict():
    request_bbody = request.get_json()
    schema = RequestSchema()
    
    try:
        # validate the request vs the schema data types
        result = schema.load(request_body)
    except ValidationError as err:
        # return a nice message if the request is not valid
        return jsonify(err.messages), 400
    
    dataset = pd.DataFrame([[request_body['Radius [cm]'],
                            request_body['Layers'],
                            request_body['Topping']]], columns=input_params)
                            
    process_dataset = preprocessing.preprocess(dataset)
    result = modelManager.predict(process_dataset)
    return jsonify({"predict_result":int(result)}, 200)

@app.route('/toppings', methods=['POST'])
def getToppings():
    return jsonify({"toppings":inputManager.get_toppings()}, 200)

@app.route('/model-info', methods=['GET'])
def getModelInfo():
    return jsonify({"model_info":modelManager.get_info()}, 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999)
    
