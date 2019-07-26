'''
Created on Jul 18, 2019
'''
from flask import Flask,jsonify, request

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)