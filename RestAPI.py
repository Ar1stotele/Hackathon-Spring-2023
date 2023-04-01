from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
totalCarbon = 20
glassBottles = 50
cans = 40
totalItems = 77
plasticBottles = 45



@app.route("/data")
def getData():
    return {"Carbon":totalCarbon, "glass":glassBottles, "cans": cans, "totalItems": totalItems, "plastic": plasticBottles}




