from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from student import Student
import os
import subprocess, sys
import cv2
import numpy as np
from tkinter import messagebox


class train:
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

        title_lb1=Label(text="TRAIN DATASET")
        title_lb1.place(x=300, y=102, width=100, height=20)
        

        img4=Image.open("colleges_images/4.jpeg")
        img4=img4.resize((200,100))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root, image=self.photoimg4, command=self.train_classifier,  cursor="hand2")
        b1.place(x=102, y=200, width=200, height=100)

        b1=Button(self.root, text="Train Data",command=self.train_classifier, cursor="hand2")
        b1.place(x=102, y=300, width=200, height=20)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file1) for file1 in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert("L")
            imageNp=np.array(img, 'uint8')
            id1=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id1)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #training and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")


# python -m pip install --user opencv-contrib-python



        
        

        
        

        
        
        

        # Function Button hifi
        # testing my laptop

    







if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()


