#!/usr/bin/env/python3

#import pygame
import subprocess
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#import conf
ffpath = "/usr/bin/"
video_conv = tkr.Tk()
video_conv.title("ffmpeg Commander - v. 0.0.1")
video_conv.geometry("600x400")
directory = askdirectory()
os.chdir(directory) # let us change the current folder
file_list = os.listdir() # equal to 'ls'
play_list = tkr.Listbox(video_conv, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)
for item in file_list:
   pos = 0
   play_list.insert(pos, item)
   pos += 1

def mp3():
 subprocess.run([ffpath+"ffmpeg", "-i", (play_list.get(tkr.ACTIVE)), (play_list.get(tkr.ACTIVE))+".mp3"])

def h264():
 subprocess.run([ffpath+"ffmpeg", "-i", (play_list.get(tkr.ACTIVE)), "-c:a", "libmp3lame", "-c:v", "libx264", (play_list.get(tkr.ACTIVE))+".mp4"])

def h265():
 subprocess.run([ffpath+"ffmpeg", "-i", (play_list.get(tkr.ACTIVE)), "-c:v", "libx265", (play_list.get(tkr.ACTIVE))+"_hevc.mkv"])

def crediti():
   crediti = tkr.Tk()
   crediti.title("About")
   crediti.geometry("400x300")
   label = tkr.Label(crediti, text="Interfaccia per un uso umano di ffmpeg.\nSviluppata in python 3 da Stefano Scalmani.\nDistribuita su licenza Creative Commons\n\"Attribuzione - Non Commerciale - Condividi allo stesso modo\".\nAttenzione: questo software è sperimentale e non offro alcuna garanzia")
   label.pack()

Button1 = tkr.Button(video_conv, width=5, height=3, font='Helvetica 12 bold', text='MP3 - solo audio', command=mp3, bg='blue', fg='white')
Button2 = tkr.Button(video_conv, width=5, height=3, font='Helvetica 12 bold', text='MP4 h264 - tracce audio mp3', command=h264, bg='red', fg='white')
Button3 = tkr.Button(video_conv, width=5, height=3, font='Helvetica 12 bold', text='MKV h265 - HEVC', command=h265, bg='purple', fg='white')
Button4 = tkr.Button(video_conv, width=5, height=3, font='Helvetica 12 bold', text='About', command=crediti, bg='cyan', fg='white')

var = tkr.StringVar()
song_title = tkr.Label(video_conv, font='Helvetica 12 bold', textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")

video_conv.mainloop()
