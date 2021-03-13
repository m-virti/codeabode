import json
from datetime import datetime,date
import pyrebase

def attcheck(j):
    if j<minatt:
        print("YOU NEED TO ATTEND ",minatt-j,"MORE LECTURES TO HAVE REQUIRED MINIMUM 75% ATTENDANCE")
    elif j==minatt:
        print("YOUR ATTENDANCE IS 75% OF REQUIRED MINIMUM ATTENDANCE\nATTEND MORE LECURES SO YOU CAN CHILL WITHOUT ANY WORRIES")
    else:
        print("YOUR ATTENDANCE IS ABOVE 75% OF REQUIRED MINIMUM ATTENDANCE\nCHILL , RELAX , CODE & KEEP VIBING")

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
counter={}
no_of_attendance_days=0
attfiles=db.get()
for date in attfiles.each():
    no_of_attendance_days+=1
    file=date.key()
    j=db.child(file).get()
    for i in j.each():
        o=i.key()
        if o in counter:
            counter[o]+=1
        else:
            counter[o]=1


print("Total numbers of days=",no_of_attendance_days)
minatt=int(0.75*no_of_attendance_days)
choice=int(input("Enter 1 to view attendance\nEnter 2 to check attendance of specific day\n"))
if choice==1:
    q=int(input("Enter 1 to view total attendance of every student\nEnter 2 to view attendance of specific student\n"))
    if q==1:
        print("Name - Numbeer of attendance")
        for n in counter:
            print(n,"-",counter[n])
            attcheck(counter[n])
    elif q==2:
        stname=input("Enter student name: ").upper()
        print(stname," - ",counter[stname])
        attcheck(counter[stname])
elif choice==2:
    day=input("Enter date in YYYY-MM-DD Format with the dash: ")
    dfile="Attendance - " + day
    spfile=db.child(dfile).get()
    print("Name - Entry time")
    try:
        for sts in spfile.each():
            print(sts.key()," - ",sts.val())
    except:
        print("Wrong date, run program again")

input()
    
           
