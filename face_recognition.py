from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from student import Student
import os
import subprocess, sys
import cv2
import numpy as np
from tkinter import messagebox
import mysql.connector as connection


class face_reco:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1150x590+0+0")
        self.root.title("face reco system")
        img1=Image.open("colleges_images/1.jpeg")
        img1=img1.resize((200,100))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root, image=self.photoimg1)
        f_lb1.place(x=0, y=0, width=200, height=100)
        
        img2=Image.open("colleges_images/2.jpeg")
        img2=img2.resize((200,100))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb2=Label(self.root, image=self.photoimg2)
        f_lb2.place(x=201, y=0, width=200, height=100)

        img3=Image.open("colleges_images/3.jpeg")
        img3=img3.resize((200,100))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lb3=Label(self.root, image=self.photoimg3)
        f_lb3.place(x=402, y=0, width=200, height=100)

        title_lb1=Label(text="FACE RECOGNITION")
        title_lb1.place(x=300, y=102, width=200, height=20)
        

        img4=Image.open("colleges_images/4.jpeg")
        img4=img4.resize((200,100))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root, image=self.photoimg4, command=self.face_recognition1, cursor="hand2")
        b1.place(x=102, y=200, width=200, height=100)

        b1=Button(self.root, text="Face Reco",command=self.face_recognition1, cursor="hand2")
        b1.place(x=102, y=300, width=200, height=20)

    #face recognition

    def face_recognition1(self):
        def draw_boundray(img, classifier, scaleFactor, minNeigh, color, text, clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image, scaleFactor, minNeigh)

            coord=[]

            for (x,y,w,h) in features:
                cv2.reactangle(img, (x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                conn = connection.connect(host="localhost",user="root", database="student1", use_pure=True)
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from StudentDetails where Studendid="+str(id))
                n=my_cursor.fectchone()
                n="+".join(n)

                my_cursor.execute("select Roll from StudentDetails where Studendid="+str(id))
                r=my_cursor.fectchone()
                r="+".join(r)

                my_cursor.execute("select Dep from StudentDetails where Studendid="+str(id))
                d=my_cursor.fectchone()
                d="+".join(d)






                if confidence>77:
                    cv2.putText(img, f"Roll:{r}", (x,y-45), cv2.FONT_HERSHEY_COMPLEX, 0.8,(25,255,0),2)
                    cv2.putText(img, f"Name:{n}", (x,y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8,(25,255,0),2)
                    cv2.putText(img, f"Dep:{d}", (x,y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8,(25,255,0),2)
                else:
                    cv2.reactangle(img, (x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img, "Unknown Face", (x,y-45), cv2.FONT_HERSHEY_COMPLEX, 0.8,(25,255,0),2)
                
                coord=[x,y,w,h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord=draw_boundray(img, faceCascade, 1.1,10,(255,255,255), "Face", clf)
            return img 
        
        faceCascade=cv2.CascadeClassifier("hass.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face reco", img)

            if cv2.waitKey(1)==13:
                break
            
            video_cap.release()
            cv2.destroyAllWindows()







        
        

        
        

        
        
        

        # Function Button hifi
        # testing my laptop

    







if __name__=="__main__":
    root=Tk()
    obj=face_reco(root)
    root.mainloop()


