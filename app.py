import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import pickle
import numpy as np
import pandas as pd

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "ml_secret_key"  # Change this!
jwt = JWTManager(app)

# curl -X POST http://127.0.0.1:5000/login -H "Content-type: application/json" -d "{\"username\" : \"dang\", \"password\" : \"vue\"}"
# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "dang" or password != "vue":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)




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
#     curl -X POST localhost:5000/api/proba -H "Content-type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NTc1MzA5NCwianRpIjoiZTIzZDVhYWUtYTBhMi00OWRmLWE0NWUtNTNhY2IxZDNiOTEzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRhbmciLCJuYmYiOjE2OTU3NTMwOTQsImV4cCI6MTY5NTc1Mzk5NH0.HKv1kYnEMwL6fVZC6UDKpll-J8S3U9FKZBEOHTk2tac" -d "{\"Sepal_Length\" : 5.1, \"Sepal_Width\" : 3.5, \"Petal_Length\" : 1.4, \"Petal_Width\" : 0.2}" 

@app.route('/api/proba', methods=['POST'])
@jwt_required()
def proba():

    print("This")
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    print(current_user)

    data = request.get_json()
    json_data = json.dumps(data)
    # print(json_data)
    dfreadjson = pd.read_json(json_data, orient='index').T
    # print(dfreadjson)
    prediction = model.predict(dfreadjson)
    _proba = model.predict_proba(dfreadjson)[:,1]
    print(prediction)

    return jsonify(model.predict_proba(dfreadjson)[:,1].tolist()), 200


if __name__ == '__main__':
    app.run(debug=True)