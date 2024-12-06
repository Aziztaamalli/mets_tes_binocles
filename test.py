from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained XGBoost model and scaler
model = joblib.load('C://Users//Hadiill//Desktop//mipi//xgboost_alert_model.pkl')
scaler = joblib.load('C://Users//Hadiill//Desktop//mipi//scaler.pkl')  # Ensure you saved the scaler in your original code

# Define a prediction endpoint
@app.route('/metrics', methods=['POST'])
def predict():
    try:
        # Get the input data from the POST request
        data = request.get_json(force=True)

        # Convert data into DataFrame
        df = pd.DataFrame(data)

        # Scale the features using the same scaler
        X_scaled = scaler.transform(df)

        # Get predictions from the model
        predictions = model.predict(X_scaled)

        # Return the prediction as JSON
        response = {
            'predictions': predictions.tolist()  # Convert numpy array to list for JSON serialization
        }
        
        print(response)
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)