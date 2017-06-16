from Tkinter import *
import tkMessageBox
import tkSimpleDialog
import sys
import numpy as np
import cv2
import tkFont

class VideoRecorder:

    def __init__(self,master):
        startVideoFrame = Frame(master)
        startVideoFrame.pack()
    
        fileName = tkSimpleDialog.askstring("Video name" , "enter file name :")
        FrameRate = tkSimpleDialog.askinteger("frame rate", "how many frame rate do you want ?")
        if FrameRate < 0:
            wrongComp = tkMessageBox.showinfo("Error","Unidentified Choice! please restart and retry.")
            sys.exit()

        CompressionMethod = tkSimpleDialog.askinteger("choose the compression method","1-DIVX\n2-XVID\n3-MJPG\n4-X264\n5-WMV1\n6-WMV2")
        if CompressionMethod == -1:
            wrongComp = tkMessageBox.showinfo("Error","Unidentified Choice! please restart and retry.")
            sys.exit()
        choosedComp = self.compressionConfig(CompressionMethod)

        savedFileName = self.fileConfig(fileName,CompressionMethod)

        #helv36 = tkFont.Font(family='Helvetica', size=40, weight='bold')
        #startRecordeButton = Button (startVideoFrame, text = 'Start Record' ,font=helv36,command =self.videoCapture(savedFileName, choosedComp, FrameRate))
        #startRecordeButton.grid(row=0, column=0, columnspan=1, sticky='EWNS')
        self.videoCapture(savedFileName, choosedComp, FrameRate)


    def videoCapture(self, fileName, compressionMethod, frameRate):
        # Open capture stream from webcam
        capture = cv2.VideoCapture(0)
        print fileName
        # Define the codec and create VideoWriter object
        """
            fourcc is a 4-byte code used to specify the video codec
            choices => DIVX, XVID, MJPG, X264, WMV1, WMV2 
        """
        fourcc = cv2.VideoWriter_fourcc(*compressionMethod)

        # VideoWriter object writes video to file, object handle is set to out
        out = cv2.VideoWriter(fileName, fourcc, frameRate, (640,480))

        # while capture stream is open
        while(capture.isOpened()):
            ret, frame = capture.read()
            if ret==True:
                # Flip frame operation example
                # frame = cv2.flip(frame,0)

                # write the frame after the operations are done
                out.write(frame)

                # Display the resulting frame (after it was written to file)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('p'):
                    cv2.waitKey(0)
                if cv2.waitKey(1) & 0xFF == ord('r'):
                    continue
                    #cv2.waitKey(1)
                if cv2.waitKey(1) & 0xFF == ord('e'):
                    cv2.destroyWindow('frame')
                    break
            else:
                break

        # Release everything after everything is done
        capture.release()
        out.release()
        cv2.destroyAllWindows()

    def compressionConfig(self, compChoice):
        if compChoice == 1:
            # DIVX
            return 'DIVX'
        elif compChoice == 2:
            # XVID
            return 'XVID'
        elif compChoice == 3:
            # MJPG
            return 'MJPG'
        elif compChoice == 4:
            # X264
            return 'X264'
        elif compChoice == 5:
            # WMV1
            return 'WMV1'
        elif compChoice == 6:
            # WMV2
            return 'WMV2'
        else:
            # bad input
            return -1

    def fileConfig(self, fileName, compChoice):
        if compChoice == 1:
            # DIVX
            return fileName + ".avi"
        elif compChoice == 2:
            # XVID
            return fileName + ".avi"
        elif compChoice == 3:
            # MJPG
            return fileName + ".mjpg"
        elif compChoice == 4:
            # X264
            return fileName + ".mp4"
        elif compChoice == 5:
            # WMV1
            return fileName + ".wmv"
        elif compChoice == 6:
            # WMV2
            return fileName + ".wmv"
        else:
            # bad input
            return -1

root = Tk()

startVideo = VideoRecorder(root)
 
root.mainloop()        
