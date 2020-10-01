import face_recognition as fr
import cv2
import numpy as np



def compare_faces(image1, image2):
    # Load the jpg files into numpy arrays
 
    
    # Get the face encodings for 1st face in each image file
    image1_encoding = fr.face_encodings(image1)[0]
    image2_encoding = fr.face_encodings(image2)[0]
    
    # Compare faces and return True / False
    results = fr.compare_faces([image1_encoding], image2_encoding)    
    return results[0]

     
known_faces = [('Kaivalya Naik','drive/My Drive/known_faces/kaivalya.jpg')]
    
def face_rec(file):
    """
    Return name for a known face, otherwise return 'Uknown'.
    """
    for name, known_file in known_faces:
        if compare_faces(known_file,file):
            return name
    return 'Unknown' 