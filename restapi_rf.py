from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the trained model
        model = joblib.load('random_forest_model.pkl')

        # Get the data from the request
        request = {
                "heartbeat": 72
            }
        data = request.json
        df = pd.DataFrame(data)

        # Make predictions
        predictions = model.predict(df)

        # Return the predictions as JSON
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
