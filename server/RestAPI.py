import cv2
import sys
import time
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

@app.route("/glass", methods=["POST", "GET"])
def updateglass():
    global glassBottles
    global totalItems
    global totalCarbon
    totalItems += 1
    glassBottles += 1
    totalCarbon += .003
    print(totalItems)
    return "SUCCESS"


@app.route("/cans", methods=["POST", "GET"])
def updateCans():
    global cans
    global totalItems
    global totalCarbon
    totalCarbon += 0.0968
    totalItems += 1
    cans += 1
    print(totalItems)
    return "SUCCESS"

@app.route("/send", methods=["POST", "GET"])
def get():
    data = request.json
    print(data)
    if data["type"] == "plastic":
        global plasticBottles
        global totalItems
        global totalCarbon
        totalCarbon += 0.828
        totalItems += 1
        plasticBottles += 1
        glassbin = cv2.imread("Images\glassbin.jpg", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Please place your waste in the Yellow, 'Glass' Bin", glassbin)
        cv2.setWindowProperty("Please place your waste in the Yellow, 'Glass' Bin", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.waitKey(1)
        time.sleep(5)
        cv2.destroyAllWindows()
        print(totalItems)
    elif data["type"] == "can":
        global cans
        global totalItems
        global totalCarbon
        totalCarbon += 0.0968
        totalItems += 1
        cans += 1
        plasticbin = cv2.imread("Images\plasticbin.jpg", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Please place your waste in the Blue, 'Plastic' Bin", plasticbin)
        cv2.setWindowProperty("Please place your waste in the Blue, 'Plastic' Bin", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.waitKey(1)
        time.sleep(5)
        cv2.destroyAllWindows()
    elif data["type"] == "glass":
        global glassBottles
        global totalItems
        global totalCarbon
        totalItems += 1
        glassBottles += 1
        totalCarbon += .003
        metalbin = cv2.imread("Images\metalbin.jpg", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Please place your waste in the Red, 'Metal' Bin", metalbin)
        cv2.setWindowProperty("Please place your waste in the Red, 'Metal' Bin", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.waitKey(1)
        time.sleep(5)
        cv2.destroyAllWindows()
        print(totalItems)

    return "SUCCESS"

@app.route("/plastic", methods=["POST", "GET"])
def updatePlastic():
    global plasticBottles
    global totalItems
    global totalCarbon
    totalCarbon += 0.828
    totalItems += 1
    plasticBottles += 1
    print(totalItems)
    return "SUCCESS"


@app.route("/data")
def getData():
    return {"Carbon":totalCarbon, "glass":glassBottles, "cans": cans, "totalItems": totalItems, "plastic": plasticBottles}
