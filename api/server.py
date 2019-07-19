'''
Created on Jul 18, 2019
'''
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/api/train")
def train():
    from training import trainModel
    message = trainModel()
    return jsonify(status = message)

@app.route("/api/assignWeightToDates")
def weightAssignment():
    from assignWeightToDates import assignWeight
    message = assignWeight()
    return jsonify(status = message)

if __name__ == "__main__":
    app.run(debug=True)