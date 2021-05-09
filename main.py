import datetime
import schedule
import time
# import keyboard
from selenium import webdriver
from info import *
from join import *

# pip install -r requirements.txt

name = "\nbot specially made to bunk the class"

datelog = datetime.datetime.now()
day = (datelog.strftime("%a"))
print(day + name)

currentTime = datelog.strftime("%H:%M:%S")
print("time:", currentTime)

''' monday'''
schedule.every().monday.at(firstClass).do(joinEnglish)
schedule.every().monday.at(secondClass).do(joinMaths)
schedule.every().monday.at(thirdClass).do(joinBio)
schedule.every().monday.at(fourthClass).do(joinPhysics)
schedule.every().monday.at(fifthClass).do(joinChem)

'''tuesday'''
schedule.every().tuesday.at(firstClass).do(joinPhysics)
schedule.every().tuesday.at(secondClass).do(joinMaths)
schedule.every().tuesday.at(thirdClass).do(joinBio)
schedule.every().tuesday.at(fourthClass).do(joinChem)
schedule.every().tuesday.at(fifthClass).do(joinEnglish)

'''wednesday'''
schedule.every().wednesday.at(firstClass).do(joinEnglish)
schedule.every().wednesday.at(secondClass).do(joinChem)
schedule.every().wednesday.at(thirdClass).do(joinPhysics)
schedule.every().wednesday.at(fourthClass).do(joinMaths)
schedule.every().wednesday.at(fifthClass).do(joinMaths)

'''thursday'''
schedule.every().thursday.at(firstClass).do(joinEnglish)
schedule.every().thursday.at(secondClass).do(joinMaths)
schedule.every().thursday.at(thirdClass).do(joinEnglish)
schedule.every().thursday.at(fourthClass).do(joinChem)
schedule.every().thursday.at(fifthClass).do(joinBio)

'''friday'''
schedule.every().friday.at(firstClass).do(joinEnglish)
schedule.every().friday.at(secondClass).do(joinChem)
schedule.every().friday.at(thirdClass).do(joinPhysics)
schedule.every().friday.at(fourthClass).do(joinMaths)
schedule.every().friday.at(fifthClass).do(joinBio)

'''saturday'''
schedule.every().saturday.at(firstClass).do(joinEnglish())
schedule.every().saturday.at(secondClass).do(joinChem)
schedule.every().saturday.at(thirdClass).do(joinPhysics)
schedule.every().saturday.at(fourthClass).do(joinMaths)
schedule.every().saturday.at(fifthClass).do(joinBio)
schedule.every().saturday.at(dummyClass).do(dummy)

'''sunday'''
schedule.every().sunday.at(dummyClass).do(dummy)

while True:
    schedule.run_pending()
    time.sleep(1)