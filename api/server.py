'''
Created on Jul 18, 2019
'''
from flask import Flask,jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,resources={r"/api/*":{"origins":"*"}})

@app.route("/api/train")
def train():
    from training import trainModel
    message = trainModel()
    return jsonify(result = message)

@app.route("/api/assignWeightToDates")
def weightAssignment():
    from assign_weight_to_dates import assignWeight
    message = assignWeight()
    return jsonify(result = message)

@app.route("/api/alternatives")
def alternatives():
    from search_and_rank_alternatives import getAlternatives
    message = getAlternatives(request.args.get("originalDrugName"))
    return jsonify(result = message)

@app.route("/api/pharmacies")
def pharmacies():
    from pharmacy_info import getPharmaciesHavingDrug
    message = getPharmaciesHavingDrug(request.args.get("drugName"))
    result = {}
    result["info"] = message[0]
    result["details"] = message[1:]
    return result

if __name__ == "__main__":
    app.run(debug=True)