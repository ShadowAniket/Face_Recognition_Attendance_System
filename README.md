
Face Recognition Attendance System
This project implements a Face Recognition Attendance System using OpenCV, Tkinter, and MySQL. It captures images, trains a face recognition model, and then uses it to recognize faces and mark attendance in real-time.

Table of Contents
Features
Technologies Used
Prerequisites
Installation
Project Structure
Usage
Acknowledgements
Features
Face Detection and Recognition: Utilizes the Haar Cascade Classifier and Local Binary Pattern Histogram (LBPH) for real-time face recognition.
Attendance Marking: Recognizes faces and marks attendance with details such as Name, Roll Number, and Department.
GUI Interface: Built with Tkinter for an easy-to-use graphical interface for managing students, training the model, and real-time attendance.
MySQL Integration: Stores student details and attendance records in a MySQL database.
Image Capture and Dataset Generation: Automatically captures and stores face images for training.
Technologies Used
Python 3.8+
OpenCV (4.5+)
Tkinter
PIL (Pillow)
NumPy
MySQL Connector
MySQL Database
Prerequisites
Before running this project, you need to have the following:

Python 3.8+ installed.
MySQL Server installed and running.
The following Python libraries:
OpenCV: pip install opencv-python opencv-contrib-python
Pillow: pip install Pillow
MySQL Connector: pip install mysql-connector-python
NumPy: pip install numpy
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/ShadowAniket/Face_Recognition_Attendance_System.git
cd Face_Recognition_Attendance_System
Install the required libraries:

bash
Copy code
pip install -r requirements.txt
Set up the MySQL Database:

Create a database named face_recogniser.

Create a table named student with the following structure:

sql
Copy code
CREATE TABLE student (
    Student_id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Roll VARCHAR(20),
    Dep VARCHAR(50)
);
Update the MySQL credentials:

In the project, find and update your MySQL username and password in the code under face_recognition.py and train.py.
Run the application:

bash
Copy code
python main.py
Project Structure
/data: Directory where face images are saved during data collection.
/attendance: Attendance records are stored here in CSV format.
/college_images: Contains images used in the Tkinter GUI.
main.py: Main file to run the GUI application.
train.py: Contains the code to train the face recognition model.
face_recognition.py: Face recognition and attendance marking logic.
Usage
Add New Students: Use the GUI to enter student details such as name, roll number, and department.
Capture Dataset: Capture student images using the webcam to create the training dataset.
Train the Model: After capturing the dataset, train the LBPH Face Recognizer by clicking the "Train Data" button.
Recognize Faces and Mark Attendance: Run face recognition and mark attendance automatically with details fetched from the MySQL database.
View Attendance: The attendance record is stored as CSV files and can be viewed or exported.
Acknowledgements
This project was inspired by the need for a contactless, automated attendance system that can be deployed in schools, colleges, or workplaces.

Special thanks to:

OpenCV for the face recognition algorithms.
Tkinter for the GUI.
MySQL for database management.
Feel free to contribute to this project by submitting issues or pull requests on GitHub.









