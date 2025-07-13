# realtime_face_recognisation
Real-Time Face Recognition Attendance System

This project implements a Real-Time Face Recognition Attendance System using OpenCV, K-Nearest Neighbors (KNN), and Streamlit for a user-friendly interface and attendance tracking. The system captures live video 
from a webcam, detects faces, stores the data, and recognizes individuals using machine learning techniques. The project is divided into three main components:

**1. Face Data Collection Script (add_faces.py)**

This script captures face images from a live webcam feed, associates them with a user name and register number, and stores the data for later recognition.

_Features:_

Uses OpenCV's Haar Cascade Classifier for face detection.

Captures 100 face samples for each user.

Stores face data, names, and register numbers in separate pickle files (faces_data.pkl, names.pkl, register_numbers.pkl).

Allows the system to accumulate data for multiple users.

**2. Web-Based Dashboard (app.py)**

The app.py script is a simple Streamlit dashboard that provides real-time updates of a counter using the FizzBuzz algorithm and displays attendance records. It automatically refreshes and shows the attendance log for the current day.

_Features:_

Displays a counter with FizzBuzz logic.

Displays attendance data from a CSV file specific to the current date.

Real-time interface using Streamlit's auto-refresh functionality.


**3. Face Recognition and Attendance System (test.py)**

This script runs the main face recognition and attendance logging functionality. It detects and recognizes faces from a live video feed and logs attendance in a CSV file.

_Features:_

Uses K-Nearest Neighbors (KNN) to classify faces in real-time.

When a face is recognized, the system logs the name and timestamp into a CSV file.

Utilizes a background image for the user interface.

Includes audio feedback for attendance confirmation using Windows Text-to-Speech (TTS).

Automatically saves attendance data in Attendance/Attendance_<date>.csv.
