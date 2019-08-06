'''
Created on Jul 18, 2019
'''
from flask import Flask,jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
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

@app.route("/api/alternatives",methods=["POST"])
def alternatives():
    from search_and_rank_alternatives import getAlternatives
    result = getAlternatives(request.json)
    return result

@app.route("/api/pharmacies")
def pharmacies():
    from pharmacy_info import getPharmaciesHavingDrug
    result = getPharmaciesHavingDrug(request.args.get("drugName"))
    return result

@app.route("/api/test",methods=["POST"])
def test():
    content = request.json;
    if request.json["info"] == True:
        print("its true")
    else:
        print("true not found")
    return jsonify(result="done")

if __name__ == "__main__":
    app.run(debug=True)