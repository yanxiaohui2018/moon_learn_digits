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


def playmp3(file):
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()
    print(file)


def playdigit0():
    playmp3("0.mp3")


def playdigit1():
    playmp3("1.mp3")


def playdigit2():
    playmp3("2.mp3")


def playdigit3():
    playmp3("3.mp3")


def playdigit4():
    playmp3("4.mp3")


def playdigit5():
    playmp3("5.mp3")


def playdigit6():
    playmp3("6.mp3")


def playdigit7():
    playmp3("7.mp3")


def playdigit8():
    playmp3("8.mp3")


def playdigit9():
    playmp3("9.mp3")


pygame.init()

root = Tk()
root.title("慕恩学数字 V1.0")
# root.geometry("400x300+0+0")
root.resizable(0, 0)

#logo = PhotoImage(file="moon.gif")
#Label(root, image=logo).pack()
Label(root,
      text="by 爸爸（颜晓辉） @哈曼国际",
      fg="light green",
      bg="dark green").pack(fill=X)

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
