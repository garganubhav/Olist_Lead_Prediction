from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn import preprocessing
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

        for i in range(len(data)):
            encoder = preprocessing.LabelEncoder()
            encoder.fit(data[i])
            data[i] = encoder.transform(data[i])

        data = np.array([data], dtype=float)

        prediction = model.predict(data)

        prediction_text = "Lead will convert {}".format(prediction[0])

        return render_template('index.html', prediction_text=prediction_text)

    return render_template('index.html')

if __name__ == '__main__':

    model = j.load(open('models/model.joblib', 'rb'))
    
    app.run(debug=True, host='0.0.0.0', port=5000)
