import time
import tkinter
from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import cv2
import os
import sys
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from dev import Dev
from time import strftime
from datetime import datetime

class Face_Recognition_System:
   def __init__(self, root): 
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recogniton System")

         #img0
         img=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\face-recognition.png")
         img=img.resize((500,130),Image.LANCZOS)
         self.photoimg=ImageTk.PhotoImage(img)

         f_lbl=Label(self.root, image=self.photoimg)
         f_lbl.place(x=0,y=0,width=500,height=130)

         #img1
         img1=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\facialrecognition.png")
         img1=img1.resize((500,130),Image.LANCZOS)
         self.photoimg1=ImageTk.PhotoImage(img1)

         f_lbl=Label(self.root, image=self.photoimg1)
         f_lbl.place(x=500,y=0,width=500,height=130)
         
         #img2
         img2=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\sample.jpg")
         img2=img2.resize((500,130),Image.LANCZOS)
         self.photoimg2=ImageTk.PhotoImage(img2)

         f_lbl=Label(self.root, image=self.photoimg2)
         f_lbl.place(x=1000,y=0,width=500,height=130)

         #bg img
         img3=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\bg2.jpeg")
         img3=img3.resize((1530,710),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=130,width=1530,height=710)

         title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("sans seriff",32,"bold"),bg="navy", fg="white")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         #time
         def show_time():
                string = time.strftime("%H:%M:%S %p")
                clock.config(text=string)
                clock.after(1000, show_time)
         clock=Label(bg_img, font=("times new roman",14,"bold"),bg="white",fg="blue")
         clock.place(x=0,y=0,width=110,height=40)
         show_time()


         #student btn
         img4=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\student-portal_1.jpg")
         img4=img4.resize((220,220),Image.LANCZOS)
         self.photoimg4=ImageTk.PhotoImage(img4)

         b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
         b1.place(x=200,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("sans seriff",15,"bold"),bg="navy", fg="azure")
         b1_1.place(x=200,y=300,width=220,height=40)
         
         
         #Detect Face btn
         img5=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\best_face_reg.jpeg")
         img5=img5.resize((220,220),Image.LANCZOS)
         self.photoimg5=ImageTk.PhotoImage(img5)

         b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
         b1.place(x=600,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data,font=("sans seriff",15,"bold"),bg="navy", fg="azure")
         b1_1.place(x=600,y=300,width=220,height=40)

         #Attendance Face btn
         img6=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\student_handraised.jpeg")
         img6=img6.resize((220,220),Image.LANCZOS)
         self.photoimg6=ImageTk.PhotoImage(img6)

         b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
         b1.place(x=1000,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("sans seriff",15,"bold"),bg="navy", fg="azure")
         b1_1.place(x=1000,y=300,width=220,height=40)

         #Help Face btn
         '''
         img7=Image.open(r"your image")
         img7=img7.resize((220,220),Image.LANCZOS)
         self.photoimg7=ImageTk.PhotoImage(img7)

         b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
         b1.place(x=1100,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Help",cursor="hand2",font=("sans seriff",15,"bold"),bg="navy", fg="azure")
         b1_1.place(x=1100,y=300,width=220,height=40)
         '''
         #Train Face btn
         img8=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\face_detector1.jpg")
         img8=img8.resize((220,220),Image.LANCZOS)
         self.photoimg8=ImageTk.PhotoImage(img8)

         b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
         b1.place(x=200,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("sans seriff",15,"bold"),bg="navy", fg="azure")
         b1_1.place(x=200,y=580,width=220,height=40)

         #Photos Face btn
         img9=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\tony.jpg")
         img9=img9.resize((220,220),Image.LANCZOS)
         self.photoimg9=ImageTk.PhotoImage(img9)

         b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
         b1.place(x=600,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("sans seriff",15,"bold"),bg="navy", fg="azure")
         b1_1.place(x=600,y=580,width=220,height=40)

         #Developer Face btn
         '''
         img10=Image.open(r"your image")
         img10=img10.resize((220,220),Image.LANCZOS)
         self.photoimg10=ImageTk.PhotoImage(img10)

         b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.dev_data)
         b1.place(x=1100,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Admin",cursor="hand2",command=self.dev_data,font=("sans seriff",15,"bold"),bg="navy", fg="azure")
         b1_1.place(x=1100,y=580,width=220,height=40)
         '''
         #Exit Face btn
         img11=Image.open(r"C:\Users\Aniket\Desktop\MiniP2A\ams\college_images\exit.jpeg")
         img11=img11.resize((220,220),Image.LANCZOS)
         self.photoimg11=ImageTk.PhotoImage(img11)

         b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
         b1.place(x=1000,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("sans seriff",15,"bold"),bg="navy", fg="azure")       
         b1_1.place(x=1000,y=580,width=220,height=40)


   def open_img(self):
         os.startfile("data")

   def iExit(self):
          self.iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to Exit")
          if self.iExit > 0:
                 self.root.destroy()
          else:
                 return
           

 #functional buttons

   def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

   def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

   def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

   def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

   def dev_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Dev(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()