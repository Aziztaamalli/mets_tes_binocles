import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the pre-trained XGBoost model and scaler
model = joblib.load('C://Users//Hadiill//Desktop//mipi//xgboost_alert_model.pkl')
scaler = joblib.load('C://Users//Hadiill//Desktop//mipi//scaler.pkl')

# Define the prediction function
def predict(data):
    try:
        # Convert input data into DataFrame
        df = pd.DataFrame(data)

        # Scale the features using the same scaler
        X_scaled = scaler.transform(df)

        # Get predictions from the model
        predictions = model.predict(X_scaled)

        # Return the prediction
        return predictions.tolist()

    except Exception as e:
        return {'error': str(e)}
