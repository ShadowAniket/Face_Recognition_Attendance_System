from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import sys
import numpy as np


class Train:
    def __init__(self, root): 
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recogniton System")

         title_lbl=Label(self.root, text="Train Dataset", font=("sans seriff",32,"bold"),bg="white", fg="navy")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         img_top=Image.open(r"college_images\facial_recognition_action.jpg")
         img_top=img_top.resize((1530,325),Image.LANCZOS)
         self.photoimg_top=ImageTk.PhotoImage(img_top)

         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0,y=55,width=1530,height=325)

         b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("sans seriff",25,"bold"),bg="green4", fg="azure")
         b1_1.place(x=00,y=380,width=1530,height=60)

         img_bottom=Image.open(r"college_images\facial-recognition_0.jpg")
         img_bottom=img_bottom.resize((1500,325),Image.LANCZOS)
         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

         f_lbl=Label(self.root,image=self.photoimg_bottom)
         f_lbl.place(x=0,y=440,width=1530,height=325)

    
    def train_classifier(self):
        data_dir=("data")
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found", parent=self.root)
            return
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        # Training the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset is Completed.")



         



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()