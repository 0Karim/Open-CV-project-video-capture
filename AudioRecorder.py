import pyaudio
import wave
from Tkinter import *
import tkMessageBox

CHUNK = 1024
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2
RATE = 44100 #sample rate
WAVE_OUTPUT_FILENAME = "output.wav"

RECORD_SECONDS = tkSimpleDialog.askinteger("Duration", "how many seconds rate do you want ?")
startRecord = tkMessageBox.showinfo("Voice Record","the record has been started.")

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data) # 2 bytes(16 bits) per channel

print("* done recording")
doneRecord = tkMessageBox.showinfo("Voice Record","Finished")


stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
