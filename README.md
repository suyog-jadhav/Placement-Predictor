# Student Placement Predictor

A machine learning web application that predicts student placement probability based on academic and extra-curricular parameters.

## Features
- Real-time placement prediction
- Interactive web interface
- Probability-based results
- Color-coded feedback system

## Technology Stack
- Backend: Flask
- ML: scikit-learn, pandas, numpy
- Frontend: HTML, CSS, JavaScript
- WSGI Server: Waitress

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/suyog-jadhav/Placement-Predictor.git
cd devl
```

2. Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

## Project Structure
```
devl/
├── app.py              # Flask application
├── train.py           # Model training script
├── requirements.txt   # Project dependencies
├── templates/         # HTML templates
├── static/           # CSS and JavaScript files
├── model.pkl         # Trained model
└── scaler.pkl        # Feature scaler
```
