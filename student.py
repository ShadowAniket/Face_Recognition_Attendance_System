from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2





class Student:
     def __init__(self, root): 
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recogniton System")

         #variables
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
        

        
        #bg img
         img3=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\bg2.jpeg")
         img3=img3.resize((1780,940),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=0,width=1780,height=940)

         title_lbl=Label(bg_img, text="Student Details", font=("sans seriff",32,"bold"),bg="white", fg="red")
         title_lbl.place(x=0,y=0,width=1530,height=45)
         
         main_frame=Frame(bg_img,bd=2,bg="white")
         main_frame.place(x=20,y=100,width=1500,height=600)
        
         #left label frame
         Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
         Left_frame.place(x=10,y=10,width=760,height=580)

        #img left
         img_left=Image.open("college_images/student_handraised.jpeg")
         img_left=img_left.resize((760,130),Image.LANCZOS)
         self.photoimg_left=ImageTk.PhotoImage(img_left)

         f_lbl=Label(Left_frame, image=self.photoimg_left)
         f_lbl.place(x=5,y=0,width=750,height=130)


        #current course
         Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
         Current_course_frame.place(x=10,y=140,width=760,height=150)
         
         #department
         dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
         dep_label.grid(row=0,column=0,padx=10,sticky=W)

         dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
         dep_combo["values"]=("Select Department","Computer","IT","Mechanical","Civil")
         dep_combo.current(0)
         dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
         course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
         course_label.grid(row=0,column=2,padx=10,sticky=W)

         course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
         course_combo["values"]=("Select Course","FE","SE","TE","BE")
         course_combo.current(0)
         course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
         year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
         year_label.grid(row=1,column=0,padx=10,sticky=W)

         year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
         year_combo["values"]=("Select Year","2022-23","2023-24","2024-25","2025-26")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #semester
         semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
         semester_label.grid(row=1,column=2,padx=10,sticky=W)

         semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
         semester_combo["values"]=("Select Semester","sem-1","sem-2","sem-3","sem-4","sem-5","sem-6","sem-7","sem-8")
         semester_combo.current(0)
         semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class_student information
         class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
         class_student_frame.place(x=10,y=250, width=760,height=300)

         #studentID
         studentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
         studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

         studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
         studentID_entry.grid(row= 0,column=1,padx=10,pady=5,sticky=W)

        #student name
         studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
         studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

         studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
         studentName_entry.grid(row= 0,column=3,padx=10,pady=5,sticky=W)

        #class division
         class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
         class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


         div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
         div_combo["values"]=("Select Division","A","B","C")
         div_combo.current(0)
         div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #roll.no
         roll_no_label=Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
         roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

         roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
         roll_no_entry.grid(row= 1,column=3,padx=10,pady=5,sticky=W)

         #Gender
         gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
         gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

         gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
         gender_combo["values"]=("Male","Female","Other")
         gender_combo.current(0)
         gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
         dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
         dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

         dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
         dob_entry.grid(row= 2,column=3,padx=10,pady=5,sticky=W)

        #Email
         email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
         email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

         email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
         email_entry.grid(row= 3,column=1,padx=10,pady=5,sticky=W)

         #phone no.
         phone_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
         phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

         phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
         phone_entry.grid(row= 3,column=3,padx=10,pady=5,sticky=W)

        #Address
         address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
         address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

         address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
         address_entry.grid(row= 4,column=1,padx=10,pady=5,sticky=W)

         #teacher name
         taecher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
         taecher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

         teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
         teacher_entry.grid(row=4 ,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
         self.var_radio1=StringVar()
         radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
         radiobtn1.grid(row=6,column=0)

         radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
         radiobtn2.grid(row=6,column=1)

        #buttons frames
         btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=0,y=200,width=715,height=35)

         save_btn=Button(btn_frame,text="save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         save_btn.grid(row=0,column=0)

         update_btn=Button(btn_frame,text="update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         update_btn.grid(row=0,column=1)

         delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         delete_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         reset_btn.grid(row=0,column=3)

         btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
         btn_frame1.place(x=0,y=235,width=715,height=35)

         take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take photo sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
         take_photo_btn.grid(row=0,column=0)
         
         update_photo_btn=Button(btn_frame1,text="update photo sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
         update_photo_btn.grid(row=0,column=1)


         #right label frame
         Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
         Right_frame.place(x=780,y=10,width=710,height=580)

         img_right=Image.open("college_images/face-recognition.png")
         img_right=img_right.resize((720,130),Image.LANCZOS)
         self.photoimg_right=ImageTk.PhotoImage(img_right)

         f_lbl=Label(Right_frame, image=self.photoimg_right)
         f_lbl.place(x=5,y=5,width=720,height=130)

         #=========search system============
         #Class_student information
         Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
         Search_frame.place(x=5,y=135, width=710,height=70)

         Search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
         Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W) 

         Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
         Search_combo["values"]=("Select ","Roll no","Phone no.")
         Search_combo.current(0)
         Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
         search_entry.grid(row= 0,column=2,padx=10,pady=5,sticky=W)

         search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
         search_btn.grid(row=0,column=3,padx=4)

         showall_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
         showall_btn.grid(row=0,column=4,padx=4)
       
        #==============table farmes========
         table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
         table_frame.place(x=5,y=210, width=710,height=350)

         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
         
         self.student_table=ttk.Treeview(table_frame,column=("Dep","course","year","sem","ID","name","div","roll_no","gender","Dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("Dep",text="Department")
         self.student_table.heading("course",text="Course")
         self.student_table.heading("year",text="Year")
         self.student_table.heading("sem",text="Sem")
         self.student_table.heading("ID",text="ID")
         self.student_table.heading("name",text="Name")
         self.student_table.heading("div",text="Division")
         self.student_table.heading("roll_no",text="Roll No")
         self.student_table.heading("gender",text="Gender")
         self.student_table.heading("Dob",text="Dob")
         self.student_table.heading("email",text="Email")
         self.student_table.heading("phone",text="Phone")
         self.student_table.heading("address",text="Address")
         self.student_table.heading("teacher",text="Teacher")
         self.student_table.heading("photo",text="Photo")
         self.student_table["show"]="headings"

         self.student_table.column("Dep",width=100)
         self.student_table.column("course",width=100)
         self.student_table.column("ID",width=100)
         self.student_table.column("name",width=100)
         self.student_table.column("div",width=100)
         self.student_table.column("roll_no",width=100)
         self.student_table.column("div",width=100)
         self.student_table.column("gender",width=100)
         self.student_table.column("phone",width=100)
         self.student_table.column("address",width=100)
         self.student_table.column("teacher",width=100)
         self.student_table.column("photo",width=150)
         
         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()

     #function declaration
     def add_data(self):
         if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
         else:
                try:
                     conn = mysql.connector.connect(
                         host="localhost",
                         username="root",
                         password="Ehusei3opqaj293@$uwi",
                         database="face_recogniser"
                         )
                     my_cursor = conn.cursor()
                     my_cursor.execute(
                         "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (
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
                            )
                        )
                     conn.commit()
                     self.fetch_data()
                     conn.close()
                     messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
                except Exception as es:
                     messagebox.showerror("Error",f"Error:{str(es)}",parent=self.root)
                     
 #fetch DB
     def fetch_data(self):
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Ehusei3opqaj293@$uwi",
                database="face_recogniser"
                )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()

            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit
            conn.close()

     #get cursor
     def get_cursor(self,event=""):
          cursor_focus=self.student_table.focus()
          contents=self.student_table.item(cursor_focus)
          data=contents["values"]
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
          self.fetch_data()
                                                             
        
     #update function
     def update_data(self):
          if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
          else:
               try:
                    update = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                    if update>0:
                         conn=mysql.connector.connect(
                              host="localhost",
                              user="root",
                              password="Ehusei3opqaj293@$uwi",
                              database="face_recogniser"
                              )
                         my_cursor=conn.cursor()
                         my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,photosample=%s where Student_id=%s",
                                           (
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
                         conn.commit()
                         self.fetch_data()
                         conn.close()
                         messagebox.showinfo("Success","Student details updated successfully",parent=self.root)

                    else:
                        if not update:
                             return
                   
               except Exception as es:
                    messagebox.showerror("Error",f"Error:{str(es)}",parent=self.root)
     
     
     #delete function     
     def delete_data(self):
          if self.var_std_id.get()=="":
               messagebox.showerror("Error","Student id is required",parent=self.root)
          else:
               try:
                    delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root)
                    if delete>0:
                         conn=mysql.connector.connect(
                              host="localhost",
                              user="root",
                              password="Ehusei3opqaj293@$uwi",
                              database="face_recogniser"
                              )
                         my_cursor=conn.cursor()
                         query="delete from student where Student_id=%s"
                         value=(self.var_std_id.get(),)
                         my_cursor.execute(query,value)
                    else:
                         if not delete:
                              return
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details deleted successfully",parent=self.root)
               except Exception as es:
                    messagebox.showerror("Error",f"Error:{str(es)}",parent=self.root)

     #reset data
     def reset_data(self):
          self.var_dep.set("Select Department")
          self.var_course.set("Select Course")
          self.var_year.set("Select Year")
          self.var_semester.set("Select Semester")
          self.var_std_id.set("")
          self.var_std_name.set("")
          self.var_div.set("Select Division")
          self.var_roll.set("")
          self.var_gender.set("Male")
          self.var_dob.set("")
          self.var_email.set("")
          self.var_phone.set("")
          self.var_address.set("")
          self.var_teacher.set("")
          self.var_radio1.set("")

     #Generationg Data set of Photos
     
     def generate_dataset(self):
          if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
          else:
               try:
                
                    conn=mysql.connector.connect(
                         host="localhost",
                         user="root",
                         password="Ehusei3opqaj293@$uwi",
                         database="face_recogniser"
                              )
                    my_cursor=conn.cursor()
                    my_cursor.execute("Select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for i in myresult:
                         id+=1
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,photosample=%s where Student_id=%s",
                                           (
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
                                                ))==id+1
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                         
                    conn.close()

                         #predefined cv2 haar frontal face
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                         


                    def face_cropped(img):
                              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                              
                              faces=face_classifier.detectMultiScale(gray,1.3,5)
                              for (x,y,w,h) in faces:
                                   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)  
                                   face_cropped= img[y:y+h,x:x+w]
                                   if detect_blur(face_cropped):
                                        continue
                                   return face_cropped,img
                              return None, img
                         
                         
                    cap=cv2.VideoCapture(0)
                         
                         

                    img_id=0
                    previous_frame=None
                    frame_count=0
                    frame_interval = 10

                        
                         
                         


                    def detect_blur(image):
                              gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                              laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
                              if laplacian_var < 100:  # Threshold to detect blur
                                   return True
                              return False

                         
                    while True:
                              ret,my_frame=cap.read()
                              if not ret:
                                   break

                              


                              cropped_face, frame_with_rectangle = face_cropped(my_frame)
                              if cropped_face is not None:
                                             
                                             img_id += 1
                                             cropped_face_gray = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2GRAY)
                                             cropped_face_resized = cv2.resize(cropped_face_gray, (450, 450))
                                             cropped_face_show = cv2.resize(cropped_face,(450,450))
                                             file_name_path = f"data/user.{id}.{img_id}.jpg"
                                             cv2.imwrite(file_name_path, cropped_face_resized)
                                             cv2.putText(cropped_face_resized, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                             cv2.imshow("Face Cropped", cropped_face_show)

                              
                              cv2.imshow("Face Detection", frame_with_rectangle)

                              #previous_frame = my_frame
                              #frame_count += 1
                              #if frame_count % 10 == 0:  # Capture every 10th frame
                                   #cv2.imshow("Frame", my_frame)

                              if cv2.waitKey(1)==13 or int(img_id)==100:
                                   break
                    my_cursor.close     
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Dataset is Generated")
               except Exception as es:
                    messagebox.showerror("Error",f"Error:{str(es)}",parent=self.root)


          




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()