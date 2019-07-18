'''
Created on Jul 18, 2019
'''
from flask import Flask,jsonify
from training import trainModel

app = Flask(__name__)

@app.route("/api/train")
def trainData():
    message = trainModel()
    if message == "Training complete":
        return jsonify(status = "training complete")
    
    return jsonify(status = "some error in training")

if __name__ == "__main__":
    app.run(debug = True)