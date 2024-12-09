#!/usr/bin/env/python3

import subprocess
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os
import settings

video_conv = Tk()
video_conv.title("ffmpeg Commander - v. 0.1.0")
video_conv.geometry("600x400")

mainframe = ttk.Frame(video_conv, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
video_conv.columnconfigure(0, weight=1)
video_conv.rowconfigure(0, weight=1)
frame1 = ttk.Frame(mainframe, width=390, padding="3 3 12 12")
frame1.grid(column=0, row=0, sticky=(N, W, E, S))
frame2 = ttk.Frame(mainframe, width=390, padding="3 3 12 12")
frame2.grid(column=0, row=1, sticky=(N, W, E, S))

in_directory = askdirectory()
os.chdir(in_directory) # let us change the current folder
file_list = os.listdir() # equal to 'ls'
play_list = Listbox(video_conv, font="Helvetica 12 bold", bg="white", width=390, selectmode=SINGLE)
for item in file_list:
   pos = 0
   play_list.insert(pos, item)
   pos += 1
opt = StringVar(value='3')
hopt = StringVar(value='o')

#def mp3():
def audio():
 if ((opt.get()) == '1'):
     subprocess.run([settings.ffpath+"ffmpeg", "-i", (play_list.get(ACTIVE)), (play_list.get(ACTIVE))+".wav"])
 else:
     subprocess.run([settings.ffpath+"ffmpeg", "-i", (play_list.get(ACTIVE)), "-c:a", "libmp3lame", "-q:a", (opt.get()), (play_list.get(ACTIVE))+".mp3"])

def h264():
    subprocess.run([settings.ffpath+"ffmpeg", "-i", (play_list.get(ACTIVE)), "-c:a", "libmp3lame", "-q:a", (opt.get()), "-c:v", "libx264", (play_list.get(ACTIVE))+".mp4"])

def h265():
 if ((hopt.get()) == 'm'):
     subprocess.run([settings.ffpath+"ffmpeg", "-i", (play_list.get(ACTIVE)), "-c:a", "libmp3lame", "-c:v", "libx265", (play_list.get(ACTIVE))+"_hevc.mkv"])
 else:
     subprocess.run([settings.ffpath+"ffmpeg", "-i", (play_list.get(ACTIVE)), "-c:v", "libx265", (play_list.get(ACTIVE))+"_hevc.mkv"])

def crediti():
   crediti = Tk()
   crediti.title("About")
   crediti.geometry("400x100")
   label = Label(crediti, text="Interfaccia per un uso umano di ffmpeg.\nSviluppata in Python v.3 da Stefano Scalmani.\nDistribuita su licenza MIT.\nAttenzione: questo software è sperimentale e\n non offro alcuna garanzia")
   label.pack()

Button1 = ttk.Button(frame1, width=30, text='Solo audio', command=audio)
Button2 = ttk.Button(frame1, width=30, text='MP4 h264 - tracce audio mp3', command=h264)
Button3 = ttk.Button(frame2, width=30, text='MKV h265 - HEVC', command=h265)
hevo = ttk.Radiobutton(frame2, text='audio OGG', variable=hopt, value='o')
hevm = ttk.Radiobutton(frame2, text='audio mp3', variable=hopt, value='m')
Button4 = ttk.Button(frame2, width=30, text='About', command=crediti)
mp3hbr = ttk.Radiobutton(frame1, text='mp3 alto bitrate', variable=opt, value='3')
mp3mbr = ttk.Radiobutton(frame1, text='mp3 medio bitrate', variable=opt, value='5')
wave = ttk.Radiobutton(frame1, text='Wav', variable=opt, value='1')
var = StringVar()
var.set(in_directory)
box_title = Label(video_conv, font='Helvetica 12 bold', textvariable=var)

box_title.grid(column=0, row=5, sticky="W")
Button1.grid(column=0, row=1, columnspan=4, sticky="W")
Button2.grid(column=0, row=2, columnspan=4, sticky="W")
Button3.grid(column=0, row=1, columnspan=4, sticky="W")
Button4.grid(column=0, row=2, columnspan=4, sticky="W")
mp3hbr.grid(column=4, row=1)
mp3mbr.grid(column=6, row=1)
wave.grid(column=8, row=1)
hevo.grid(column=4, row=1)
hevm.grid(column=6, row=1)
play_list.grid(column=0, row=6, columnspan=4, sticky="W, S")

video_conv.mainloop()
