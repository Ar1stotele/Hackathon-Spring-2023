# TACO (Garbage) Detection (SSD MobileNet v2) with TensorFlow

import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from google.protobuf import text_format
import pprint
import json
import os
from object_detection.utils import label_map_util
from object_detection.protos import string_int_label_map_pb2
import cv2
from pyzbar import pyzbar
import keyboard
import time
import requests
import json


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')
        print(barcode_info)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        # 3
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
            # return the bounding box of the barcode
    return frame

cam = cv2.VideoCapture(0)

#Don't touch anything until the comment near the bottom
def reconstruct(pb_path):
    if not os.path.isfile(pb_path):
        print("Error: %s not found" % pb_path)

    print("Reconstructing Tensorflow model")
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.io.gfile.GFile(pb_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    print("Success!")
    return detection_graph

def image2np(image):
    (w, h) = image.size
    return np.array(image.getdata()).reshape((h, w, 3)).astype(np.uint8)

def image2tensor(image):
    npim = image2np(image)
    return np.expand_dims(npim, axis=0)

def detect(detection_graph, test_image_path):
    with detection_graph.as_default():
        gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.01)
        with tf.compat.v1.Session(graph=detection_graph,config=tf.compat.v1.ConfigProto(gpu_options=gpu_options)) as sess:
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            image = Image.open(test_image_path)
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image2tensor(image)}
            )
            class_squeeze = np.squeeze(classes).astype(np.int32)[0] #represents the item with the highest score, so the ome the AI sees most in the image
            score_squeeze = np.squeeze(scores)[0] #represents the score of the item with the highest score
            return {'mainItem': class_squeeze, 'confidence': score_squeeze}

# Create LabelMap


DATA_DIR = 'aistuff'
ANNOTATIONS_FILE = os.path.join(DATA_DIR, 'annotations_3_test.json')
NCLASSES = 60

with open(ANNOTATIONS_FILE) as json_file:
    data = json.load(json_file)
    
categories = data['categories']

print('Building label map from examples')

labelmap = string_int_label_map_pb2.StringIntLabelMap()
for idx,category in enumerate(categories):
    item = labelmap.item.add()
    # label map id 0 is reserved for the background label
    item.id = int(category['id'])+1
    item.name = category['name']

with open('./labelmap.pbtxt', 'w') as f:
    f.write(text_format.MessageToString(labelmap))

print('Label map witten to labelmap.pbtxt')

with open('./labelmap.pbtxt') as f:
    pprint.pprint(f.readlines())

label_map = label_map_util.load_labelmap('labelmap.pbtxt')
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NCLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


detection_graph = reconstruct("aistuff/ssd_mobilenet_v2_taco_2018_03_29.pb")

# ----------------------------------------------------------------------------------------------------------------
# Everything below here should be all the code you need to work with
def displayImage(image):
    glassbin = cv2.imread(image, cv2.IMREAD_ANYCOLOR)
    cv2.imshow("output", glassbin)
    cv2.setWindowProperty("output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)
    time.sleep(5)

url = 'http://10.35.96.149:5000/send'
aiEnabled = False
barcodeArr = {'0070847811169': 'can', '0078000003864': 'plastic'}
aiData = {"Drink can": 'can', "Disposable plastic cup": 'can', "Food can": 'can', "Plastic film": 'plastic', "Clear plastic bottle": 'plastic', 'Aerosol': 'can'}
images = {'can': 'display\Images\metalbin.jpg', 'plastic': 'display\Images\plasticbin.jpg', 'glass': 'display\Images\glassbin.jpg'}
while True:
    if keyboard.is_pressed("space"):
        aiEnabled = not aiEnabled
        print("aiEnabled:", aiEnabled)
        time.sleep(1)
    success, image = cam.read()
    if success:
        ret, frame = cam.read()
        cv2.imwrite("img.jpg", image)
        # ['mainItem'] is the item most recognized in the current frame by the AI, ['confidence'] is the AI's confidence that's it's correct about what it labels the item as
        if aiEnabled:
            detectResults = detect(detection_graph, 'img.jpg')
            if detectResults['mainItem'] > 1 and detectResults['confidence'] > 0.70: # if trash found with an at least 20% confidence
                itemName = categories[detectResults['mainItem']-1]['name']
                print (itemName)
                print (detectResults['confidence']) 
                for item in aiData:
                    if itemName == item:
                        displayImage(images[aiData[item]])
                        data = {'type': aiData[item]}
                        json_data = json.dumps(data)
                        headers = {'Content-type': 'application/json'}
                        response = requests.post(url, data=json_data, headers=headers)
                        print(response.status_code)
                        print(response.content) 
            else: #no trash found
                print ("no trash found")
        else:
            codes = pyzbar.decode(frame)
            for barcode in codes:
                for bc in barcodeArr:
                    if barcode.data.decode("utf-8") == bc:
                        displayImage(images[barcodeArr[bc]])
                        data = {'type': barcodeArr[bc]}
                        json_data = json.dumps(data)
                        headers = {'Content-type': 'application/json'}
                        response = requests.post(url, data=json_data, headers=headers)
                        print(response.status_code)
                        print(response.content)
            frame = read_barcodes(frame)
        cv2.imshow('output', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        time.sleep(.5)
    else:
        print("no cam :(")
    #time.sleep(1)    