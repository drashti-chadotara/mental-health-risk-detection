from flask import Flask, render_template, request, send_from_directory
import joblib
import os
from utils import get_result_content

app = Flask(__name__)

# Load trained ML model
model = joblib.load('../model/mental_health_model.pkl')

# Serve images
@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'images'), filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    # ✅ request MUST be used inside this function
    values = [
        int(request.form['Growing_Stress']),
        int(request.form['Mood_Swings']),
        int(request.form['Days_Indoors']),
        int(request.form['Coping_Struggles']),
        int(request.form['Social_Weakness']),
        int(request.form['Work_Interest'])
    ]

    total_score = sum(values)

    # ✅ SMART HYBRID LOGIC
    if total_score <= 2:
        risk_level = "Low Risk"
    elif 3 <= total_score <= 6:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    content = get_result_content(risk_level)

    return render_template(
        'result.html',
        risk_level=risk_level,
        greeting=content['greeting'],
        message=content['message'],
        suggestions=content['suggestions'],
        image=content['image'],
        video=content['video']
    )

if __name__ == '__main__':
    app.run(debug=True)
