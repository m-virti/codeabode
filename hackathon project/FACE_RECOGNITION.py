import cv2
import numpy as np
import os
import face_recognition as fr
from datetime import datetime,date
import json
import pyrebase

#funtion to encode the image/frames captured
def encode(image):
    elist=[]
    for img in image:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encoding=fr.face_encodings(img)[0]
        elist.append(encoding)
    return elist

def Attendance(name):
    dic[name]=datetime.now().strftime('%H: %M: %S')
    db.child("Attendance - " + str(date.today())).update(dic)
    

firebaseConfig = {
    'apiKey': "AIzaSyDN8RS4oH4ltiolizl5qlalijb5Z_0VHTc",
    'authDomain': "attendance-codeabode.firebaseapp.com",
    'databaseURL': "https://attendance-codeabode-default-rtdb.firebaseio.com",
    'projectId': "attendance-codeabode",
    'storageBucket': "attendance-codeabode.appspot.com",
    'messagingSenderId': "513633578274",
    'appId': "1:513633578274:web:a7699b11fc658ca11e097b"
  }
fb=pyrebase.initialize_app(firebaseConfig)
db=fb.database()
dic={}

path=r'faces'
image=[]
fnames=[]
myfiles=os.listdir(path)
for i in myfiles:
    curimg=cv2.imread(f'{path}/{i}')
    image.append(curimg)
    fnames.append(os.path.splitext(i)[0])
print(fnames)

encodedlist=encode(image)
print("ENCODING COMPLETED...")

cap=cv2.VideoCapture(0)

while True:
    success, img=cap.read()
    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    faceframe=fr.face_locations(imgs)
    encodeframe=fr.face_encodings(imgs,faceframe)
    for encodeface,faceloc in zip(encodeframe,faceframe):
        matches=fr.compare_faces(encodedlist,encodeface)
        facedis=fr.face_distance(encodedlist,encodeface)
        print(facedis)
        matchindex=np.argmin(facedis)

        if matches[matchindex]:
            name=fnames[matchindex].upper()
            print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)
            Attendance(name)
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
