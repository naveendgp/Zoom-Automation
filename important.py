# this file controls web browsers, any change to this file may break whole program
import keyboard

import time

import pyautogui


def zoomJoin():
    time.sleep(5)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)

def joinaAudio():
    time.sleep(3)
    audio = pyautogui.locateOnScreen('join audio.png')
    if audio == True:
        pyautogui.click(audio)
    else:
        ok = pyautogui.locateOnScreen('ok.png')
        pyautogui.click(ok)

def msTeams():
    time.sleep(6)  # takes time to load cam and glitches sometimes so i set it higher
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)  # turning off mic
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)  # turning off cam
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)  # join
