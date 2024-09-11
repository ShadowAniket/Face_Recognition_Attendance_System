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
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root): 
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recogniton System")

         #variables
         self.var_attendanceID=StringVar()
         self.var_atten_roll=StringVar()
         self.var_atten_name=StringVar()
         self.var_atten_dep=StringVar()
         self.var_atten_date=StringVar()
         self.var_atten_time=StringVar()
         self.var_atten_status=StringVar()
         


         #bg img
         img3=Image.open(r"college_images\bg2.jpeg")
         img3=img3.resize((1780,940),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=0,width=1780,height=940)

         title_lbl=Label(bg_img, text="Student Attendance ", font=("sans seriff",32,"bold"),bg="red", fg="white")
         title_lbl.place(x=0,y=0,width=1530,height=45)
         
         main_frame=Frame(bg_img,bd=2,bg="white")
         main_frame.place(x=20,y=100,width=1480,height=600)

         #left label frame
         Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
         Left_frame.place(x=10,y=10,width=760,height=580)

        
         img_left=Image.open("college_images/student_handraised.jpeg")
         img_left=img_left.resize((760,130),Image.LANCZOS)
         self.photoimg_left=ImageTk.PhotoImage(img_left)

         f_lbl=Label(Left_frame, image=self.photoimg_left)
         f_lbl.place(x=5,y=0,width=750,height=130)

         left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
         left_inside_frame.place(x=0,y=135,width=720,height=370)

         #Label and entry
         # attendance id

         attendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
         attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

         attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attendanceID,width=20,font=("times new roman",12,"bold"))
         attendanceID_entry.grid(row= 0,column=1,padx=10,pady=5,sticky=W)

         # roll id

         rolllabel=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
         rolllabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

         atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
         atten_roll.grid(row= 0,column=3,padx=10,pady=5,sticky=W)

         # name id

         namelabel=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
         namelabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

         atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
         atten_name.grid(row= 1,column=1,padx=10,pady=5,sticky=W)

         # department id

         deplabel=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
         deplabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

         atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
         atten_dep.grid(row= 1,column=3,padx=10,pady=5,sticky=W)

         # date id

         datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
         datelabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

         atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
         atten_date.grid(row= 2,column=1,padx=10,pady=5,sticky=W)

         # time id

         timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
         timelabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

         atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
         atten_time.grid(row= 2,column=3,padx=10,pady=5,sticky=W)

         # attendance radio

         attendanceLabel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
         attendanceLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

         self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_status,font=("times new roman",12,"bold"),state="readonly",width=18)
         self.atten_status["values"]=("Status","Present","Absent")
         self.atten_status.current(0)
         self.atten_status.grid(row=3,column=1,padx=10,pady=10,sticky=W)

         #buttons frames
         btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=0,y=300,width=715,height=35)

         import_Csv=Button(btn_frame,text="Import Csv",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         import_Csv.grid(row=0,column=0)

         export_Csv=Button(btn_frame,text="Export csv",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         export_Csv.grid(row=0,column=1)

         update_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         update_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,text="Reset",command=self.reset,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
         reset_btn.grid(row=0,column=3)


         #right label frame
         Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
         Right_frame.place(x=780,y=10,width=710,height=580)

         img_right=Image.open("college_images/face-recognition.png")
         img_right=img_right.resize((720,130),Image.LANCZOS)
         self.photoimg_right=ImageTk.PhotoImage(img_right)

         f_lbl=Label(Right_frame, image=self.photoimg_right)
         f_lbl.place(x=5,y=5,width=720,height=130)

         table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
         table_frame.place(x=5,y=5,width=700,height=455)

         #scroll bar table
         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         
         scroll_x.config(command=self.AttendanceReportTable.xview)
         scroll_y.config(command=self.AttendanceReportTable.yview)

         #heading
         self.AttendanceReportTable.heading("id",text="ID")
         self.AttendanceReportTable.heading("roll",text="Roll No")
         self.AttendanceReportTable.heading("name",text="Name")
         self.AttendanceReportTable.heading("department",text="Department")
         self.AttendanceReportTable.heading("time",text="Time")
         self.AttendanceReportTable.heading("date",text="Date")
         self.AttendanceReportTable.heading("attendance",text="Attendance")
         self.AttendanceReportTable["show"]="headings"
         
         self.AttendanceReportTable.column("id",anchor=CENTER,width=100)
         self.AttendanceReportTable.column("roll",anchor=CENTER,width=100)
         self.AttendanceReportTable.column("name",anchor=CENTER,width=100)
         self.AttendanceReportTable.column("department",anchor=CENTER,width=100)
         self.AttendanceReportTable.column("time",anchor=CENTER,width=100)
         self.AttendanceReportTable.column("date",anchor=CENTER,width=100)
         self.AttendanceReportTable.column("attendance",anchor=CENTER,width=100)
         self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #fetch data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    
        
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,"w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")    
        except Exception as es: 
            messagebox.showerror("Error",f"Data not exported due to {str(es)}",parent=self.root)

    def get_cursor(self,evemt=""):
      cursor_row = self.AttendanceReportTable.focus()
      contents = self.AttendanceReportTable.item(cursor_row)
      row = contents["values"]
      self.var_attendanceID.set(row[0])
      self.var_atten_roll.set(row[1])
      self.var_atten_name.set(row[2])
      self.var_atten_dep.set(row[3])
      self.var_atten_time.set(row[4])
      self.var_atten_date.set(row[5])
      self.var_atten_status.set(row[6])

    #reset 
    def reset(self):
        self.var_attendanceID.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")
        #self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()