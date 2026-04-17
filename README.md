🌾 Crop Recommendation System using Machine Learning
📌 Overview

This project is a Machine Learning-based Crop Recommendation System that predicts the most suitable crop based on soil and environmental conditions such as:

Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
pH level
Rainfall

The system uses a Random Forest Classifier trained on agricultural data and exposes predictions via a FastAPI backend.

🚀 Features
🌱 Predicts best crop for given soil conditions
🤖 Machine Learning model using Random Forest
⚡ FastAPI backend for real-time predictions
📊 Swagger UI for easy API testing (/docs)
💾 Serialized model using .pkl
🔗 Ready for frontend / IoT integration

🧠 Machine Learning Model
Algorithm Used:
Random Forest Classifier
Why Random Forest?
High accuracy on structured/tabular data
Handles non-linear relationships
Reduces overfitting using ensemble learning


📂 Project Structure

agro_smart/
│
├── app.py                  # FastAPI backend
├── crop_model.pkl         # Trained ML model
├── requirements.txt       # Dependencies
└── README.md              # Project documentation


⚙️ Tech Stack
Python 🐍
FastAPI ⚡
Scikit-learn 🤖
NumPy 🔢
Uvicorn 🌐
Pandas 📊


📊 Dataset

The model is trained using a crop recommendation dataset containing:
| Feature     | Description              |
| ----------- | ------------------------ |
| N           | Nitrogen content in soil |
| P           | Phosphorus content       |
| K           | Potassium content        |
| Temperature | In °C                    |
| Humidity    | Relative humidity        |
| pH          | Soil acidity/alkalinity  |
| Rainfall    | Rainfall in mm           |


🧪 How It Works
Input Soil Data → FastAPI → ML Model → Prediction → Crop Output

▶️ How to Run Locally

1️⃣ Clone Repository
git clone https://github.com/AmishAwasthi27/agro_smart.git
cd agro_smart

2️⃣ Install Dependencies
pip install fastapi uvicorn numpy scikit-learn

3️⃣ Run FastAPI Server
python -m uvicorn app:app

4️⃣ Open API Docs
http://127.0.0.1:8000/docs

📡 API Endpoints
🔹 Home
GET /
Response:
{
  "message": "Crop Recommendation API is running"
}

🔹 Predict Crop
POST /predict
Request Body:
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 22,
  "humidity": 80,
  "ph": 6.5,
  "rainfall": 200
}
Response:
{
  "recommended_crop": "rice"
}

🧠 Model Training (Overview)
The model was trained using:

Data preprocessing
Train-test split
Random Forest Classifier
Accuracy evaluation
Model serialization using pickle

💡 Future Improvements
🌐 Deploy API on cloud (Render / AWS)
📱 Mobile app integration
🌦 Weather API integration
📡 IoT-based soil sensor input (ESP32)
📊 Web dashboard (React / Streamlit)

🚀 Final Note

This system demonstrates a complete Machine Learning + Backend Integration pipeline, suitable for:

Academic projects
Final year engineering projects
IoT agriculture systems
AI/ML portfolio building
