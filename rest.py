from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
totalCarbon = 0
glassBottles = 0
cans = 0
totalItems = 0
plasticBottles = 0

@app.route("/send", methods=["POST", "GET"])
def send():
    data = request.json
    print(data)
    if data["type"] == "plastic":
        global plasticBottles
        global totalItems
        global totalCarbon
        totalCarbon += 0.00828
        totalItems += 1
        plasticBottles += 1
        print(totalItems)
    elif data["type"] == "can":
        global cans
        totalCarbon += 0.00968
        totalItems += 1
        cans += 1
        totalCarbon += 0.5
    return "SUCCESS"
    

# @app.route("/glass", methods=["POST"])
# def updateglass():
#     glassBottles = glassBottles + 1
#     print(glassBottles)

# @app.route("/carbon", methods=["POST"])
# def updateCarbon():
#     totalCarbon = totalCarbon + 1

# @app.route("/cans", methods=["POST"])
# def updateCans():
#     cans = cans + 1

# @app.route("/total", methods=["POST"])
# def updateItems():
#     totalItems = totalItems + 1

# @app.route("/plastic", methods=["POST"])
# def updatePlastic():
#     plasticBottles = plasticBottles + 1


@app.route("/data")
def getData():
    print({"totalCarbon":totalCarbon, "cans": cans, "totalItems": totalItems, "plasticBottles": plasticBottles})
    return {"totalCarbon":totalCarbon, "cans": cans, "totalItems": totalItems, "plasticBottles": plasticBottles}