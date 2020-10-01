from flask import Flask, request
import json
from face_util import compare_faces, face_rec
import cv2
import numpy as np

app = Flask(__name__)


def read_img(img):
    
    (h, w) = img.shape[:2]
    width = 500
    ratio = width / float(w)
    height = int(h * ratio)
    return cv2.resize(img, (width, height))


@app.route("/face_match",methods=['POST'])
def face_match():
	if(request.method == 'POST'):
		file1=request.files['file1']
		file2=request.files['file2']
		npimg1=np.fromfile(file1,np.uint8)
		img1=cv2.imdecode(npimg1,cv2.IMREAD_COLOR)
		npimg2=np.fromfile(file2,np.uint8)
		img2=cv2.imdecode(npimg2,cv2.IMREAD_COLOR)
		value=compare_faces(read_img(img1),read_img(img2))
		if(value):
			return json.dumps(True)
		else:
			return json.dumps(False)




app.run(host='0.0.0.0', port='5001', debug=True)