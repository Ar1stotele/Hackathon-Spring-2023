import time
import sys # to access the system
import cv2

from flask import Flask

app = Flask(__name__)

@app.route("/glass", methods=["POST", "GET"])
def displayGlass():
    glassbin = cv2.imread("Images\glassbin.jpg", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("Please place your waste in the Yellow, 'Glass' Bin", glassbin)
    cv2.setWindowProperty("Please place your waste in the Yellow, 'Glass' Bin", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)
    time.sleep(5)
    cv2.destroyAllWindows()
    return "success"

@app.route("/plastic", methods=["POST", "GET"])
def displayPlastic():
    plasticbin = cv2.imread("Images\plasticbin.jpg", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("Please place your waste in the Blue, 'Plastic' Bin", plasticbin)
    cv2.setWindowProperty("Please place your waste in the Blue, 'Plastic' Bin", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)
    time.sleep(5)
    cv2.destroyAllWindows()
    return "success"

@app.route("/metal", methods=["POST", "GET"])
def displayMetal():
    metalbin = cv2.imread("Images\metalbin.jpg", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("Please place your waste in the Red, 'Metal' Bin", metalbin)
    cv2.setWindowProperty("Please place your waste in the Red, 'Metal' Bin", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)
    time.sleep(5)
    cv2.destroyAllWindows()
    return "success"