from configs import data_config, preprocessing_config, model_config
from marshmallow import ValidationError
from src.collect_data import CollectData
from src.model import Model
from src.preprocessing import Preprocessing
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, request, jsonify
import pandas as pd

from src.validation import RequestSchema

app = Flask(__name__)

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


inputManager = CollectData(data_config)
preprocessing = Preprocessing(preprocessing_config)
modelManager = Model(model_config)
inputs_params = ['Radius [cm]', 'Layers', 'Topping']

@app.route('/predict', methods=['GET'])
def getPredict():
    request_body = request.json
    schema = RequestSchema()

    try:
        # Validate request body against schema data types
        result = schema.load(request_body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    dataset = pd.DataFrame([[request_body['Radius [cm]'],
                            request_body['Layers'],
                            request_body['Topping']]], columns = inputs_params)

    process_dataset = preprocessing.processData(dataset)
    result = modelManager.predict(process_dataset)
    return jsonify({"predict_result":int(result[0])}, 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)