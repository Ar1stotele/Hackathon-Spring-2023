from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

totalCarbon = 0
glassBottles = 0
cans = 0
totalItems = 0
plasticBottles = 0

@app.route("/glass", methods=["POST", "GET"])
def updateglass():
    global glassBottles
    global totalItems
    totalItems += 1
    glassBottles += 1
    print(totalItems)
    return "SUCCESS"

@app.route("/carbon", methods=["POST", "GET"])
def updateCarbon():
    global totalCarbon
    global totalItems
    totalItems += 1
    totalCarbon += 1
    print(totalItems)
    return "SUCCESS"

@app.route("/cans", methods=["POST", "GET"])
def updateCans():
    global cans
    global totalItems
    totalItems += 1
    cans += 1
    print(totalItems)
    return "SUCCESS"



@app.route("/plastic", methods=["POST", "GET"])
def updatePlastic():
    global plasticBottles
    global totalItems
    totalItems += 1
    plasticBottles += 1
    print(totalItems)
    return "SUCCESS"


@app.route("/data")
def getData():
    return {"Carbon":totalCarbon, "glass":glassBottles, "cans": cans, "totalItems": totalItems, "plastic": plasticBottles}







