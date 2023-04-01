from flask import Flask

app = Flask(__name__)

totalCarbon = 20
glassBottles = 50
cans = 40
totalItems = 77
plasticBottles = 45



@app.route("/data")
def getData():
    return {"Carbon":totalCarbon, "glass":glassBottles, "cans": cans, "totalItems": totalItems, "plastic": plasticBottles}




