#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:04:07 2017

@author: felipecrispim
"""

import sys
import dlib
from skimage import io
import numpy as np
#import openface

# You can download the required pre-trained face detection model here:
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)

win = dlib.image_window()

# Take the image file name from the command line
file_name = "/home/felipecrispim/keras-workspace/KinFaceW-I/images/father-dau/fd_003_1.jpg"

# Load the image
image = io.imread(file_name)

# Run the HOG face detector on the image data
detected_faces = face_detector(image, 1)

print("Found {} faces in the image file {}".format(len(detected_faces), file_name))

# Show the desktop window with the image
win.set_image(image)

new_face_rect = dlib.rectangle(0, 0, 64, 64)
pose_landmarks = face_pose_predictor(image, new_face_rect)
win.add_overlay(pose_landmarks)


# Loop through each face we found in the image
for i, face_rect in enumerate(detected_faces):

    # Detected faces are returned as an object with the coordinates 
    # of the top, left, right and bottom edges
    print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))

    # Draw a box around each face we found
    win.add_overlay(face_rect)

    # Get the the face's pose
    pose_landmarks = face_pose_predictor(image, face_rect)

    
    vec = np.empty([68, 2], dtype = int)
    for b in range(68):
        vec[b][0] = pose_landmarks.part(b).x
        vec[b][1] = pose_landmarks.part(b).y

    print(vec[33])  
    
    # Draw the face landmarks on the screen.
    win.add_overlay(pose_landmarks)
    
    #cv2.imwrite("aligned_face_{}.jpg".format(i), alignedFace)
    # Use openface to calculate and perform the face alignment

dlib.hit_enter_to_continue()