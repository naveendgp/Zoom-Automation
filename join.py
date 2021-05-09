
import important
from info import *
from selenium import webdriver
import time


def joinEnglish():
    driver = webdriver.Chrome('D:\\web driver\\chromedriver.exe')#enter the path where you stored you're chrome driver
    driver.get(english)
    time.sleep(5) #seconds
    important.zoomJoin()#If you're using google meet just replace zoomJoin() with google_meet()
    time.sleep(3)
    important.joinaAudio()
    time.sleep(4200)#you can change this according to your class timing
    driver.quit()

def joinPhysics():
    driver = webdriver.Chrome('D:\\web driver\\chromedriver.exe')#enter the path where you stored you're chrome driver
    driver.get(physics)
    time.sleep(5)  # seconds
    important.zoomJoin()#If you're using google meet just replace zoomJoin() with google_meet()
    time.sleep(3)
    important.joinaAudio()
    time.sleep(4200)  # you can change this according to your class timing
    driver.quit()

def joinChem():
    driver = webdriver.Chrome('D:\\web driver\\chromedriver.exe')#enter the path where you stored you're chrome driver
    driver.get(chemistry)
    time.sleep(5)  # seconds
    important.zoomJoin()#If you're using google meet just replace zoomJoin() with google_meet()
    time.sleep(3)
    important.joinaAudio()
    time.sleep(4200)  # you can change this according to your class timing
    driver.quit()

def joinMaths():
    driver = webdriver.Chrome('D:\\web driver\\chromedriver.exe')#enter the path where you stored you're chrome driver
    driver.get(maths)
    time.sleep(5)  # seconds
    important.zoomJoin()#If you're using google meet just replace zoomJoin() with google_meet()
    time.sleep(3)
    important.joinaAudio()
    time.sleep(4200)  # you can change this according to your class timing
    driver.quit()

def joinBio():
    driver = webdriver.Chrome('D:\\web driver\\chromedriver.exe')#enter the path where you stored you're chrome driver
    driver.get(biology)
    time.sleep(5)  # seconds
    important.zoomJoin()#If you're using google meet just replace zoomJoin() with google_meet()
    time.sleep(3)
    important.joinaAudio()
    time.sleep(4200)  # you can change this according to your class timing
    driver.quit()

def dummy():
    driver = webdriver.Chrome('D:\\web driver\\chromedriver.exe')#enter the path where you stored you're chrome driver
    driver.get(dummyClass)
    time.sleep(5)  # seconds
    important.zoomJoin()#If you're using google meet just replace zoomJoin() with google_meet()
    time.sleep(3)
    important.joinaAudio()
    time.sleep(4200)  # you can change this according to your class timing
    driver.quit()










def zoomJoin():
    print("inside zoom")
