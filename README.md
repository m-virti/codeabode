[Jahnvi's Resume (1).pdf](https://github.com/jahnviseth/codeabode/files/6135562/Jahnvi.s.Resume.1.pdf)
# codeabode
PROJECT DEFINITION:-
We are making an Automatic Attendance System via Facial Recognition (AASFR). Our main goal is to make a system where students' attendance is automatically taken by recognizing their faces. It will also help teachers and students to keep track of their attendance as well.

APPROACH:-
The approach idea is pretty much simple, the cameras are fitted at the entrance in the classes of the college premises. As a person passes by the camera visions, their face gets identified by our program and their attendance is taken and stored in the database.

As our project is a demo version, we are using pc webcams to identify person's faces and taking their attendance in the firebase realtime database.

FACE_RECOGNITION.PY program recognizes faces(from the faces folder) and takes a person's attendance with the time on the consequent date.

It uses the face_recognition library which works by finding faces in the picture. Find and manipulate facial features in pictures, identify faces in the pictures.

Judges can take face pics from the test images folder and show them to the webcam through their mobile(screen reflection may cause some problems).
Judges can even put their own faces in the faces folder and get their faces recognized(through webcam) and thus attendance is taken.

ATTENDANCE_VIEWER.PY program lets the users check attendance of "students ".
Users can view :
1) Attendance of specific date.
2) Total Attendance of every student.
3) Attendance of a specific student.

It even tells the percentage of students' attendance and how many lectures they need to attend to reach the minimum required attendance(75%).

If judges want to, they can view the database in the browser(use firefox for proper view and navigation) directly without the help of our program using the below link:
https://attendance-codeabode-default-rtdb.firebaseio.com/.json

TECH STACK USED:
PYTHON 3.9, FIREBASE REALTIME DATABASE, OPENCV.

VIDEO OF OUR PROJECT:
https://drive.google.com/file/d/1Pt0YhJkeh-52Xe-TDqE1d96jeAEU8ERW/view?usp=sharing

LINKS:-
Member1: JAHNVI SETH
GitHub: https://github.com/jahnviseth
LinkedIn: www.linkedin.com/in/jahnvi-seth-241638202
Resume: [jahnviresume.pdf](https://github.com/jahnviseth/codeabode/files/6135566/jahnviresume.pdf)

Member2:NISCHAY GUPTA
GitHub: https://github.com/NickDL29
LinkedIn: https://www.linkedin.com/in/nischay29/
Resume: [nischayresume.pdf](https://github.com/jahnviseth/codeabode/files/6135503/nischayresume.pdf)

Member3: DIVYANSH KUMAR MAHAVAR
GitHub: https://github.com/divyanshkm
LinkedIn: https://www.linkedin.com/in/divyanshkm/
Resume: [divyanshresume.pdf](https://github.com/jahnviseth/codeabode/files/6135493/divyanshresume.pdf)

Member4: VIRTI MEHTA
GitHub:
LinkedIn:
Resume:

INSTRUCTIONS:-
run run.cmd file first to install necessary libraries. If there is an issue with it then you may open run.cmd file in notepad and then execute statements one by one on cmd manually.

You can run FACE_RECOGNITION.py for face identification and attendance taking. Even try to add your own face pic in the faces folder and try to get your face identified. You can close the program directly by just clicking on red X on the top right window of cmd or Alt+F4.

To view attendance, run ATTENDANCE_VIEWER.py and follow its menu.
Alternatively, you can also view it on https://attendance-codeabode-default-rtdb.firebaseio.com/.json in the firefox browser.
