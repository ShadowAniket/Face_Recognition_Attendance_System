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


class Face_Recognition:
    def __init__(self, root): 
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recogniton System")

         title_lbl=Label(self.root, text="Face Recognition", font=("sans seriff",32,"bold"),bg="white", fg="darkgreen")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         img_left=Image.open(r"college_images\face_detector1.jpg")
         img_left=img_left.resize((650,700),Image.LANCZOS)
         self.photoimg_left=ImageTk.PhotoImage(img_left)

         f_lbl=Label(self.root,image=self.photoimg_left)
         f_lbl.place(x=0,y=55,width=650,height=700)
         
         img_right=Image.open(r"college_images\facialrecognition (1).png")
         img_right=img_right.resize((950,700),Image.LANCZOS)
         self.photoimg_right=ImageTk.PhotoImage(img_right)

         f_lbl=Label(self.root,image=self.photoimg_right)
         f_lbl.place(x=650,y=55,width=950,height=700)

         b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("sans seriff",15,"bold"),bg="green4", fg="azure")
         b1_1.place(x=380,y=620,width=200,height=40)

    #attendance
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(("," ))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                


    #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):  
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(
                         host="localhost",
                         user="root",
                         password="Ehusei3opqaj293@$uwi",
                         database="face_recogniser"
                              )
                my_cursor=conn.cursor()

                try:
                    my_cursor.execute("Select Name from student where Student_id="+str(id))
                    n=my_cursor.fetchone()
                    n = n[0] if n else "Unknown"
                    #n="+".join(n)
                    #either this line or above line, this was commented because it was showing exception indefinitely when no face was detected, hence opted for above line

                    my_cursor.execute("Select Roll from student where Student_id="+str(id))
                    r=my_cursor.fetchone()
                    r = r[0] if r else "Unknown"
                    #r="+".join(r)

                    my_cursor.execute("Select Dep from student where Student_id="+str(id))
                    d=my_cursor.fetchone()
                    d = d[0] if d else "Unknown"
                   # d="+".join(d)

                    my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                    i=my_cursor.fetchone()
                    i = i[0] if i else "Unknown"
                    #i="+".join(i)
                
                except Exception as e:
                    print(f"Database error: {e}")
                    n, r, d = "Unknown", "Unknown", "Unknown"
                finally:
                    my_cursor.close()
                    conn.close()


                if confidence>77:
                    cv2.putText(img,f"ID: {i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        #return coord
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()