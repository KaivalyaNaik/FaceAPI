from flask import Flask,request
import json
import cv2
import numpy as np

app = Flask(__name__)


def read_img(img):    
    (h, w) = img.shape[:2]
    width = 500
    ratio = width / float(w)
    height = int(h * ratio)
    return cv2.resize(img, (width, height))

@app.route("/take_image",methods=['POST'])
def take_image():
	if(request.method=='POST'):
		  file =request.files['file']
		  npimg=np.fromfile(file,np.uint8)
		  img=cv2.imdecode(npimg,cv2.IMREAD_COLOR)
		  read_img(img)
		  return '''hello'''

app.run(host='0.0.0.0', port='5001', debug=True)