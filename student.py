from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as connection

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1230x730+0+0")
        self.root.title("face reco system")
        
        # variable

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


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
        f_lb4.place(x=4, y=0, width=500, height=70)

        current_course_frame=LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=4, y=80, width=530, height=100)
        
        dep_label=Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row = 0, column = 0, padx=2, sticky=W)


        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="read only")
        dep_combo['values']=("Select Department", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=4, sticky=W)


        course_label=Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row = 0, column = 2, padx=2, sticky=W)


        course_combo=ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="read only")
        course_combo['values']=("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=4, sticky=W)

        year_label=Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row = 1, column = 0, padx=2, sticky=W)


        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="read only")
        year_combo['values']=("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2, pady=4, sticky=W)

        semester_label=Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row = 1, column = 2, padx=2, sticky=W)


        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="read only")
        semester_combo['values']=("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=4, sticky=W)

        class_student_frame=LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Class Student information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=4, y=185, width=530, height=300)
        
        studentId_label=Label(class_student_frame, text="StudentID", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row = 0, column = 0, padx=2, sticky=W)
        studentID_entry=ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=4, pady=2, sticky=W)

        studentName_label=Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row = 0, column = 2, padx=2, sticky=W)
        studentName_entry=ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=4, pady=2, sticky=W)
        
        class_div_label=Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row = 1, column = 0, padx=2, sticky=W)
        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=4, pady=2, sticky=W)

        roll_no_label=Label(class_student_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row = 1, column = 2, padx=2, sticky=W)
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=4, pady=2, sticky=W)

        gender_label_label=Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label_label.grid(row = 2, column = 0, padx=2, sticky=W)
        gender_label_entry=ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
        gender_label_entry.grid(row=2, column=1, padx=4, pady=2, sticky=W)

        dob_label=Label(class_student_frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row = 2, column = 2, padx=2, sticky=W)
        dob_entry=ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=4, pady=2, sticky=W)


        email_label=Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row = 3, column = 0, padx=2, sticky=W)
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=4, pady=2, sticky=W)

        phone_label=Label(class_student_frame, text="Phone No", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row = 3, column = 2, padx=2, sticky=W)
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=4, pady=2, sticky=W)


        address_label=Label(class_student_frame, text="Adress", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row = 4, column = 0, padx=2, sticky=W)
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=4, pady=2, sticky=W)

        teacher_label=Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row = 4, column = 2, padx=2, sticky=W)
        teacher_entry=ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=4, pady=2, sticky=W)
        

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No photo sample", value="No")
        radiobtn2.grid(row=6, column=1)


        #button frames

        btn_frame=Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=160, width=520, height=80)
        
        save_btn=Button(btn_frame, text="Save",command=self.add_data,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame, text="Update",command=self.update_data,font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame, text="Delete",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        delete_btn.grid(row=0, column=3)

        reset_btn=Button(btn_frame, text="Reset",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        reset_btn.grid(row=0, column=4)

        take_photo_btn=Button(btn_frame, text="Take Photo Sample",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn=Button(btn_frame, text="Update Photo Sample",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        update_photo_btn.grid(row=1, column=1)
        
        
        
        #right frame
        
        right_frame=LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=570, y=10, width=550, height=500)

        img5=Image.open("colleges_images/12.jpeg")
        img5=img5.resize((200,100))
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lb5=Label(right_frame, image=self.photoimg5)
        f_lb5.place(x=4, y=0, width=500, height=100)
         
        # Search system

        search_frame=LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE, text="Class Student information", font=("times new roman", 12, "bold"))
        search_frame.place(x=4, y=104, width=530, height=60)

        search_label=Label(search_frame, text="Search By", font=("times new roman", 12, "bold"), bg="black", fg="white")
        search_label.grid(row =0, column = 0, padx=2, sticky=W)


        search_combo=ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="read only")
        search_combo['values']=("Select", "Roll_No", "Phone NO")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2, pady=4, sticky=W)
        
        search_entry=ttk.Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=4, pady=2, sticky=W)

        search_btn=Button(search_frame, text="Search",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=8)
        search_btn.grid(row=0, column=3)

        showAll_btn=Button(search_frame, text="Show All",font=("times new roman", 12, "bold"), bg="blue", fg="white", width=8)
        showAll_btn.grid(row=0, column=4)

        table_frame=LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE)
        table_frame.place(x=4, y=170, width=530, height=300)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll","gender","dob","email", "phone","address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            # messagebox.showinfo("Success","Welcome to")
            try:
                conn = connection.connect(host="localhost",user="root", database="student1", use_pure=True)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into StudentDetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due To :{str(e)}", parent=self.root)

    def fetch_data(self):
        conn = connection.connect(host="localhost",user="root", database="student1", use_pure=True)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from StudentDetails")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])       

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to update student details", parent=self.root)
                if update>0:
                    conn = connection.connect(host="localhost",user="root", database="student1", use_pure=True)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update StudentDetails set Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s, Gender=%s,Dob=%s,Email=%s,Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Studentid=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student details successfully update completed",parent=self.root )
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Duo to: {str(e)}", parent=self.root)
        












if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()




