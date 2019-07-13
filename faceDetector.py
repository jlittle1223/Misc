import numpy as np
import cv2 as cv


file_path = "pictures/jesse.jpg"


face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')


img = cv.imread(file_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

height, width = img.shape[:2]
scale = 0.5


faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(300, 300),
    flags=cv.CASCADE_SCALE_IMAGE
)

print("found {} faces!".format(len(faces)))


for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(70, 70))
    print("found {} eyes!".format(len(eyes)))
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    


img = cv.resize(img, (int(width * scale), int(height * scale)))

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()


