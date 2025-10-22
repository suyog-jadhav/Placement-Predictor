from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging
import os
from waitress import serve
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load the model and scaler
try:
    logger.info("Loading model and scaler...")
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    logger.info("Model and scaler loaded successfully")
except FileNotFoundError as e:
    logger.error(f"Error: Model files not found - {str(e)}")
    print("Please run train_model.py first to create model.pkl and scaler.pkl")
    exit(1)
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    exit(1)

# ...rest of your existing app.py code...

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json(force=True)
        
        # Create features list in correct order
        features = [
            data['CGPA'],
            data['Internships'],
            data['Projects'],
            data['Workshops_Certifications'],
            data['AptitudeTestScore'],
            data['SoftSkillsRating'],
            1 if data['ExtracurricularActivities'] == 'Yes' else 0,
            1 if data['PlacementTraining'] == 'Yes' else 0,
            data['SSC_Marks'],
            data['HSC_Marks']
        ]
        
        # Convert to DataFrame
        features_df = pd.DataFrame([features], columns=[
            'CGPA', 'Internships', 'Projects', 'Workshops/Certifications',
            'AptitudeTestScore', 'SoftSkillsRating', 'ExtracurricularActivities',
            'PlacementTraining', 'SSC_Marks', 'HSC_Marks'
        ])
        
        # Scale features
        features_scaled = scaler.transform(features_df)
        
        # Make prediction
        prediction = model.predict(features_scaled)
        
        # Get prediction probability
        probability = model.predict_proba(features_scaled)[0][1]
        
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': float(probability)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)