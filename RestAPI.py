from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
totalCarbon = 0
glassBottles = 0
cans = 0
totalItems = 0
plasticBottles = 0

@app.route("/glass")
def updateglass():
    glassBottles = glassBottles + 1
    print(glassBottles)

@app.route("/carbon", methods=["POST"])
def updateCarbon():
    totalCarbon = totalCarbon + 1

@app.route("/cans", methods=["POST"])
def updateCans():
    cans = cans + 1

@app.route("/total", methods=["POST"])
def updateItems():
    totalItems = totalItems + 1

@app.route("/plastic", methods=["POST"])
def updatePlastic():
    plasticBottles = plasticBottles + 1


@app.route("/data")
def getData():
    return {"Carbon":totalCarbon, "glass":glassBottles, "cans": cans, "totalItems": totalItems, "plastic": plasticBottles}




