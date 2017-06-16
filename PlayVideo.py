from Tkinter import *
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import tkMessageBox
import tkSimpleDialog
import numpy as np
import cv2



class PlayVideo:
    # constructor
    def __init__(self, master):
        master.title("Play Video (^_^)")
        startVideoFrame = Frame(master)
        startVideoFrame.pack()
    
        fileName = tkSimpleDialog.askstring("Video name" , "enter file name :")
        self.videoPlay(fileName)

    def videoPlay(self, videoName):
        # Open capture stream from file
        capture = cv2.VideoCapture(videoName)

        # While capture stream is opened(reading from file)
        while(capture.isOpened()):
            ret, frame = capture.read()

            # perform operations on each frame

            # Grayscale filter effect
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Open window to show each frame
            # add operation effect as parameter => cv2.imshow('frame', gray)
            cv2.imshow('frame', frame)
            cv2.waitKey(80)
            if 0xFF == ord('q'):
                break

        # after all operations are done, release capture stream
        capture.release()
        cv2.destroyAllWindows()

root = Tk()

startVideo = PlayVideo(root)
