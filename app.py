from flask import Flask, request
from flask_cors import CORS
app = Flask (__name__)
CORS(app)

import numpy as np
import cv2
from PIL import Image
from model import *

# 28*28 흑백 이미지로 변환
def image_convert(img):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    img = cv2.resize(np.array(img), (28, 28), interpolation=cv2.INTER_AREA)
    img = 255 - (img)
    img = img / 255
    img.reshape((28, 28, 1))
    return img

@app.route('/check', methods=['GET'])
def check():
    return 'Ready'

@app.route('/predict', methods=['POST'])
def predict():
    img = image_convert(Image.open(request.files['file'].stream))
    if(np.sum(img)<1.0): return "?, ?"
    result = pred(img)
    answer = np.argmax(result)
    prob = result[0][answer] * 100.0
    return str(answer) + ", " + str(round(prob, 2))

if __name__ == "__main__":
    app.run()