#!/usr/bin/python3

# Moon Learn Digits

from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext
import serial
import serial.tools.list_ports
from time import sleep
import _thread
import re
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import xlrd
import pygame
import os
import pexpect
from evdev import InputDevice
from select import select
#import pyaudio
#import wave


def playwav(file):
    print(file)
    # define stream chunk
    chunk = 1024

    # open a wav format music
    f = wave.open(r"0.wav", "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)

    # play stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()


def playfile(file):
    print(file)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(0.5)
    pygame.mixer.music.stop()


def playdigit0():
    playfile("0.wav")


def playdigit1():
    playfile("1.wav")


def playdigit2():
    playfile("2.wav")


def playdigit3():
    playfile("3.wav")


def playdigit4():
    playfile("4.wav")


def playdigit5():
    playfile("5.wav")


def playdigit6():
    playfile("6.wav")


def playdigit7():
    playfile("7.wav")


def playdigit8():
    playfile("8.wav")


def playdigit9():
    playfile("9.wav")


def playchinesevoice(key):
    # filter out undefined keys
    if (key==0):
        return

    filename = key + '.wav'  # '.mp3'
    playfile(filename)


def scankeythread(threadname, delay):
    # always scanning digit keys
    key_code =  (82, 79, 80, 81, 75, 76, 77, 71, 72, 73,   78,    74,      55,   98,    83,      96,    103,  108,  105,  106,69,110,102,104,111,107,109,70,119)
    key_value = ('0','1','2','3','4','5','6','7','8','9','jia','jian','cheng','chu','dian','dengyu','shang','xia','zuo','you', 0,  0,  0,  0,  0,  0,  0, 0,  0)
    key_dict = dict(list(zip(key_code, key_value)))
    dev = InputDevice('/dev/input/event9')  # --office keyboard # event19--home keyboard # event4--home keypad
    while True:
        select([dev], [], [])
        for event in dev.read():
            if (event.value == 1 or event.value == 0) and event.code != 0:
                print("Key: %s Status: %s" % (event.code, "pressed" if event.value else "release"))
                if (event.code == 59):  # F1: switch to English voice
                    # playenglishvoice(scankey)
                    break

                if (event.value == 1):
                    '''
                    if (event.code <= 11):
                        if (event.code == 11):
                            scankey = 0
                        else:
                            scankey = event.code-1
                    else:
                    '''
                    scankey = key_dict[event.code]
                    print(scankey)
                    playchinesevoice(scankey)


pygame.init()
# initialize the mixer module
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

# os.system("sudo chmod 777 /dev/input/event19")

# run: linux shell sudo
'''
shell_cmd = "sudo chmod 777 /dev/input/event19"
child = pexpect.spawn(shell_cmd)
index = child.expect(['password', pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
    child.sendline("howareyou")
'''

root = Tk()
root.title("慕恩学键盘 V1.0")
# root.geometry("400x300+0+0")
root.resizable(0, 0)

logo = PhotoImage(file="moon.gif")
Label(root, image=logo).pack()
Label(root,
      text="by 爸爸（颜晓辉） @哈曼国际",
      fg="light green",
      bg="dark green").pack(fill=X)

_thread.start_new_thread(scankeythread, ("", 0))

# draw digits: 0~9
digitframe = LabelFrame(root, text="数字", bg="light blue")
digitframe.pack()

button0 = Button(digitframe, text='0', width=5, command=playdigit0)
button0.grid(row=0, column=0)

button1 = Button(digitframe, text='1', width=5, command=playdigit1)
button1.grid(row=0, column=1)

button2 = Button(digitframe, text='2', width=5, command=playdigit2)
button2.grid(row=0, column=2)

button3 = Button(digitframe, text='3', width=5, command=playdigit3)
button3.grid(row=0, column=3)

button4 = Button(digitframe, text='4', width=5, command=playdigit4)
button4.grid(row=0, column=4)

button5 = Button(digitframe, text='5', width=5, command=playdigit5)
button5.grid(row=0, column=5)

button6 = Button(digitframe, text='6', width=5, command=playdigit6)
button6.grid(row=0, column=6)

button7 = Button(digitframe, text='7', width=5, command=playdigit7)
button7.grid(row=0, column=7)

button8 = Button(digitframe, text='8', width=5, command=playdigit8)
button8.grid(row=0, column=8)

button9 = Button(digitframe, text='9', width=5, command=playdigit9)
button9.grid(row=0, column=9)

root.mainloop()
