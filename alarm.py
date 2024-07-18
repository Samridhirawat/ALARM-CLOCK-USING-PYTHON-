from playsound import playsound
import datetime
alarmHour=int(input("enter hour: "))
alarmMin=int(input("Enter Minutes: "))
alarmAm=input("am /pm: ")
if alarmAm=="pm":
  alarmHour+=12
while True:
  if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
    print("playing..........")
    playsound("alarm.mp3")
    break  