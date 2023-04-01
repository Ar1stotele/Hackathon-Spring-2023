from flask import Flask

app = Flask(__name__)




@app.route("/getCarbon")
def hello_world():
    return "<p>Hello, world!</p>"


@app.route("/getMoney")
def getMoney():
    return "This is your money"


@app.route("numberRecycled")
def getNumberRecycled():
    return "Number recycled"