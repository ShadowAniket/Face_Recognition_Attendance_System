from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import sys
import numpy as np

class Dev:
    def __init__(self, root): 
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recogniton System")

         title_lbl=Label(self.root, text="Developer", font=("sans seriff",32,"bold"),bg="white", fg="red")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         img_top=Image.open(r"college_images\bg2.jpg")
         img_top=img_top.resize((1530,720),Image.LANCZOS)
         self.photoimg_top=ImageTk.PhotoImage(img_top)

         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0,y=55,width=1530,height=720)

         #frame
         main_frame=Frame(f_lbl,bd=2,bg="white")
         main_frame.place(x=1000,y=0,width=500,height=200)

         img_in=Image.open(r"college_images\Team-Management-Software-Development.jpg")
         img_in=img_in.resize((200,200),Image.LANCZOS)
         self.photoimg_in=ImageTk.PhotoImage(img_in)

         f_lbl=Label(main_frame,image=self.photoimg_in)
         f_lbl.place(x=300,y=0,width=200,height=200)
         
         #Dev info

         dev_label=Label(main_frame,text="Hello this is Dev page.",font=("times new roman",12,"bold"),bg="white")
         dev_label.place(x=0,y=5)

         dev_label=Label(main_frame,text="This is my sem5 project. ",font=("times new roman",12,"bold"),bg="white")
         dev_label.place(x=0,y=40)

         dev_label=Label(main_frame,text="Python Opencv-Haarcascade. ",font=("times new roman",12,"bold"),bg="white")
         dev_label.place(x=0,y=75)

         dev_label=Label(main_frame,text="Github:ShadowAniket ",font=("times new roman",12,"bold"),bg="white")
         dev_label.place(x=0,y=110)




if __name__ == "__main__":
    root=Tk()
    obj=Dev(root)
    root.mainloop()