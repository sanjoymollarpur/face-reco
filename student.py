from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1200x690+0+0")
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
        f_lb2.place(x=401, y=0, width=200, height=100)

        img3=Image.open("colleges_images/3.jpeg")
        img3=img3.resize((200,100))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lb3=Label(self.root, image=self.photoimg3)
        f_lb3.place(x=802, y=0, width=200, height=100)

        title_lb1=Label(text="Student Management System")
        title_lb1.place(x=300, y=109, width=300, height=20)

        main_frame=Frame(self.root, bd=2, bg='white')
        main_frame.place(x=0, y=129, width=1190, height=550)
        
        left_frame=LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=550, height=500)


        img4=Image.open("colleges_images/10.jpeg")
        img4=img4.resize((200,100))
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lb4=Label(left_frame, image=self.photoimg4)
        f_lb4.place(x=4, y=0, width=500, height=100)

        left_frame1=LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        left_frame1.place(x=4, y=104, width=530, height=130)
        
        dep_label=Label(left_frame1, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row = 0, column = 1, pady = 2)

        right_frame=LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=570, y=10, width=550, height=500)





if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


