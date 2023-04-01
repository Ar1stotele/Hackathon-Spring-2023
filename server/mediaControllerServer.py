from flask import Flask, request, jsonify
import pyautogui

app = Flask(__name__)

@app.route('/', methods=['POST']) 
def run():
    data = request.json
    print(data['text'][0:2])
    if (data['text'][0:2] == '||'):
        pyautogui.press(data['text'][2:])
    else:
        pyautogui.write(data['text'])
    return (data)