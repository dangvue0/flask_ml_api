import json
from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



model = pickle.load(open('ml/model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    np_features = [np.array(float_features)]
    prediction = model.predict(np_features)
    prediction = prediction[0]

    return render_template('index.html', context=f'Predicted Class: {prediction}')



# ADDING NEW ENDPOINT
#     curl -X POST -H "Content-type: application/json" -d "{\"Sepal_Length\" : 5.1, \"Sepal_Width\" : 3.5, \"Petal_Length\" : 1.4, \"Petal_Width\" : 0.2}" "localhost:5000/api/proba"

@app.route('/api/proba', methods=['POST'])
def proba():

    print("This")

    data = request.get_json()
    json_data = json.dumps(data)
    # print(json_data)
    dfreadjson = pd.read_json(json_data, orient='index').T
    # print(dfreadjson)
    prediction = model.predict(dfreadjson)
    _proba = model.predict_proba(dfreadjson)[:,1]
    print(prediction)

    return str(_proba), 200


if __name__ == '__main__':
    app.run(debug=True)