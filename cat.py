# -*- coding=utf-8 -*-
import cv2

# Load the face cascade classifier
catPath = "haarcascade_frontalcatface.xml"
faceCascade = cv2.CascadeClassifier(catPath)

# Read the image and convert to gray scale
img = cv2.imread("cat1.jpg")  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the cat face
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor= 1.02,
    minNeighbors=3,
    minSize=(150, 150),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Draw a rectangle over the cat face and label it
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(img, 'Cat', (x, y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

# Save the cat image
#cv2.imshow('Cat?', img)
cv2.imwrite("cat33.jpg",img)
#c = cv2.waitKey(0)