from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib as j
import json

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def get():
    return "Healthy"


@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        
        data = [
        request.form['business_segment'],
        request.form['lead_type'],
        request.form['lead_behaviour_profile'],
        request.form['business_type'],
        request.form['landing_page_id'],
        request.form['origin']
        ]
        data = np.array([data], dtype=float)

        prediction = model.predict(data)

        prediction_text = "Lead will convert{}".format(prediction[0])

        return render_template('index.html', prediction_text=prediction_text)

    return render_template('index.html')

if __name__ == '__main__':

    model = j.load(open('models/model.joblib', 'rb'))
    
    app.run(debug=True, host='0.0.0.0', port=5000)
