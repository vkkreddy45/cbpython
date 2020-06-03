from tkinter import *
from cv2 import cv2
from PIL import Image           # pip install pillow
from PIL import ImageTk
import threading

class DetectionView:
    stop = False

    def load(self):
        window = Tk()
        window.title("Cheating Detection App")
        frame = Frame(window,bg="yellow",padx=10,pady=10)
        frame.grid(row=0,column=0,padx=10,pady=10)

        self.l1 = Label(frame)
        self.l1.grid(row=0,column=0,columns=2)

        b1 = Button(frame, text="start",command= self.startCamera)
        b1.grid(row=1,column=0)

        b2 = Button(frame, text="stop", command=self.stopCamera)
        b2.grid(row=1, column=1)

        self.startCamera()
        window.mainloop()

    def startCamera(self):
        self.stop = False
        
        # create an instance for video capture via webcam
        self.cap = cv2.VideoCapture(0)

        #  start the process by threading - to run processes parallely
        t = threading.Thread(target=self.webcam,args=())
        t.start()


    def webcam(self):

        # capture each frame (image)
        ret, frame = self.cap.read()
        frame = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
        # change the color to RBG
        colorimg = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        # converting the image to tkinter compatible image
        img = Image.fromarray(colorimg)
        imgtk = ImageTk.PhotoImage(img)

        # push the image into the tkinter label
        self.l1.config(image=imgtk)
        self.l1.image = imgtk

        # loop this process for every 10ms
        if self.stop == False:
            self.l1.after(10,self.webcam)
        else:
            self.l1.image = None

    def stopCamera(self):
        self.stop = True










