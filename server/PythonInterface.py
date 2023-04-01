from flask import Flask

app = Flask(__name__)

carbonEmissions = 0
money = 0
numberRecycled = 0

@app.route("/getCarbon")
def getCarbon():
    return str(carbonEmissions)


@app.route("/getMoney")
def getMoney():
    return str(money)


@app.route("/numberRecycled")
def getNumberRecycled():
    return str(getNumberRecycled)