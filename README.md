![ml logo](media/cake.jpeg)

# Cake Price Prediction API

A Flask-based REST API that leverages machine learning to predict cake prices based on specifications like size, layers, and toppings. Built with scikit-learn and Flask, this API provides accurate price estimates for cake orders.

## 🚀 Features

- RESTful API endpoints for cake price predictions
- Input validation and error handling
- Swagger UI documentation
- Pre-trained machine learning model
- Standardized data preprocessing pipeline
- JSON request/response format

## 🛠️ Technology Stack

- **Framework**: Flask
- **ML Libraries**: scikit-learn, pandas, numpy
- **Documentation**: Swagger/OpenAPI
- **Validation**: Marshmallow
- **Data Format**: JSON

## 📦 Project Structure

```
.
├── configs/            # Configuration files
├── data/              # Training data
├── models/            # Trained ML models
├── notebooks/         # Jupyter notebooks
├── src/              # Source code
│   ├── preprocessing.py
│   ├── model.py
│   ├── validation.py
│   └── ...
├── static/           # Static files (Swagger)
├── main.py          # Application entry point
└── requirements.txt  # Dependencies
```

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cake-price-api-predictor.git
cd cake-price-api-predictor
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # Unix/macOS
# or
.venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Running the API

1. Start the Flask server:
```bash
python main.py
```

The server will start on `http://localhost:3000`

## 📝 API Usage

### Predict Cake Price

**Endpoint**: `POST /predict`

**Request Format**:
```json
{
    "radius": 17.5,
    "layers": 2,
    "topping": "Simple"
}
```

**Response Format**:
```json
{
    "predict_result": 311.5,
    "input_data": {
        "radius": 17.5,
        "layers": 2,
        "topping": "Simple"
    }
}
```

### Available Topping Types:
- Simple
- Writing
- Picture
- Decorative
- Extreme

## 📚 API Documentation

Access the Swagger UI documentation at: `http://localhost:3000/swagger`

## 🧪 Model Training

The model was trained on a dataset of cake orders with the following features:
- Radius (cm): Size of the cake
- Layers: Number of cake layers
- Topping: Type of decoration/topping
- Price: Target variable

To retrain the model:
1. Update the training data in `data/Cakes Exercise.csv`
2. Run the training notebook in `notebooks/Cakes Model Exercise.ipynb`
3. The new model files will be saved in the `models/` directory

## 🛡️ Error Handling

The API includes comprehensive error handling for:
- Invalid input validation
- Missing required fields
- Out-of-range values
- Internal processing errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Roey Zalta (@roy2392)

## 🙏 Acknowledgments

- Special thanks to anyone who contributed to the project
- Any third-party libraries or tools used
- Inspiration sources

