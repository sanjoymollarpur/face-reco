from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk

class Face_Recognition_System:
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

        title_lb1=Label(text="Face Reco")
        title_lb1.place(x=300, y=102, width=100, height=20)
        

        img4=Image.open("colleges_images/4.jpeg")
        img4=img4.resize((200,100))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root, image=self.photoimg4, cursor="hand2")
        b1.place(x=102, y=200, width=200, height=100)

        b1=Button(self.root, text="Student Details", cursor="hand2")
        b1.place(x=102, y=300, width=200, height=20)

        img5=Image.open("colleges_images/5.jpeg")
        img5=img5.resize((200,100))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(self.root, image=self.photoimg5, cursor="hand2")
        b2.place(x=353, y=200, width=200, height=100)

        b2=Button(self.root, text="Face Detector", cursor="hand2")
        b2.place(x=353, y=300, width=200, height=20)

        img6=Image.open("colleges_images/6.jpeg")
        img6=img6.resize((200,100))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(self.root, image=self.photoimg6, cursor="hand2")
        b3.place(x=603, y=200, width=200, height=100)

        b3=Button(self.root, text="Attendance", cursor="hand2")
        b3.place(x=603, y=300, width=200, height=20)

        img7=Image.open("colleges_images/7.jpeg")
        img7=img7.resize((200,100))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(self.root, image=self.photoimg7, cursor="hand2")
        b4.place(x=843, y=200, width=200, height=100)
        b4=Button(self.root, text="Help Desk", cursor="hand2")
        b4.place(x=843, y=300, width=200, height=20)


        img8=Image.open("colleges_images/8.jpeg")
        img8=img8.resize((200,100))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b8=Button(self.root, image=self.photoimg8, cursor="hand2")
        b8.place(x=102, y=350, width=200, height=100)

        b8=Button(self.root, text="Train Data", cursor="hand2")
        b8.place(x=102, y=450, width=200, height=20)

        img9=Image.open("colleges_images/9.jpeg")
        img9=img9.resize((200,100))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b9=Button(self.root, image=self.photoimg9, cursor="hand2")
        b9.place(x=353, y=350, width=200, height=100)

        b9=Button(self.root, text="Photos", cursor="hand2")
        b9.place(x=353, y=450, width=200, height=20)

        img10=Image.open("colleges_images/11.jpeg")
        img10=img10.resize((200,100))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b10=Button(self.root, image=self.photoimg10, cursor="hand2")
        b10.place(x=603, y=350, width=200, height=100)

        b10=Button(self.root, text="Developer", cursor="hand2")
        b10.place(x=603, y=450, width=200, height=20)

        img11=Image.open("colleges_images/12.jpeg")
        img11=img11.resize((200,100))
        self.photoimg11=ImageTk.PhotoImage(img11)
        b11=Button(self.root, image=self.photoimg11, cursor="hand2")
        b11.place(x=843, y=350, width=200, height=100)
        b11=Button(self.root, text="Exit", cursor="hand2")
        b11.place(x=843, y=450, width=200, height=20)






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


