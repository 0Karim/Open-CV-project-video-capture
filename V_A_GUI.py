from Tkinter import *
import tkMessageBox
import tkSimpleDialog
import sys
import numpy as np
import cv2
import tkFont
#import pyaudio
import wave

class startPage : 
    def __init__(self,master):
        master.title("Welcome Video & Audio Recorder (^_^)")
        startFrame = Frame(master)
        startFrame.pack()
        helv36 = tkFont.Font(family='Helvetica', size=80, weight='bold')
        startButton = Button (startFrame, text = 'Start' ,font=helv36,command =self.getStart)
        startButton.grid(row=0, column=0, columnspan=1, sticky='EWNS')
        quitButton = Button (startFrame, text = 'Quit' ,font=helv36,command =master.destroy)
        quitButton.grid(row=1, column=0, columnspan=1, sticky='EWNS')

    def getStart(self):
        top = Toplevel()
        top.title("Video or Audio (^_^) ")
#        top.geometry("300x300")
        helv36 = tkFont.Font(family='Helvetica', size=50, weight='bold')
        #video
        videoButton = Button(top, text="VIDEO", font=helv36, command = self.callVideo)
        videoButton.grid(row=0, column=0, columnspan=1, sticky='EWNS')
        #audio
        audioButton = Button(top, text="AUDIO",font=helv36, command = self.callAudio)
        audioButton.grid(row=1, column=0, columnspan=1, sticky='EWNS')
        #play video
        playButton = Button(top, text="Play Video",font=helv36,command =self.callPlayVideo)
        playButton.grid(row=4, column=0, columnspan=1, sticky='EWNS')
        #back
        backButton = Button(top, text="Back", font=helv36,command =top.destroy)
        backButton.grid(row=3, column=0, columnspan=1, sticky='EWNS')
        #quit
        #quitButton = Button(top, text="Quit",font=helv36,command =top.destroy)
        #quitButton.grid(row=4, column=0, columnspan=1, sticky='EWNS')

    def callVideo(self):
        execfile("videoRecorderM.py")

    def callAudio(self):
        execfile("AudioRecorder.py")

    def callPlayVideo(self):
        execfile("PlayVideo.py")


root = Tk()

start = startPage(root)
 
root.mainloop()
