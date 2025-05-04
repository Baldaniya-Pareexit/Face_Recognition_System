# Face_Recognition_System

## **Overview:**

This project is a face recognition-based attendance system built using Python. It utilizes the face_recognition library to detect and recognize faces from a webcam feed, logs attendance with timestamps in a CSV file, and displays real-time feedback on the video feed. The system is designed to mark attendance for known individuals by comparing their faces against pre-loaded images.

## **Features:**





Captures video from a webcam and detects faces in real-time.



Recognizes known faces using pre-loaded face encodings.



Logs attendance with the name and timestamp in a CSV file named by the current date (e.g., 2025-05-04.csv).



Displays the recognized person's name and "Present" status on the video feed.



Removes recognized individuals from the student list to avoid duplicate entries.

## **Requirements:**

To run this project, you need to install the following dependencies:





Python 3.x



Libraries:





face_recognition



opencv-python (cv2)



numpy



csv (included in Python standard library)



datetime (included in Python standard library)

You can install the required libraries using pip:

pip install face_recognition opencv-python numpy

Additionally, ensure you have:





A webcam connected to your system.



A directory named faces/ containing images of known individuals (e.g., pareexit.jpg).

## **Setup:**





**1. Clone the Repository:**

git clone https://github.com/your-username/face-recognition-attendance.git
cd face-recognition-attendance



**2. Prepare the Faces Directory:**





Create a faces/ directory in the project root.



Place images of known individuals in the faces/ directory (e.g., pareexit.jpg).



Update the face_recognition.py script to load the correct image filenames and assign appropriate names in the known_face_names list.



**3. Run the Script:**

python face_recognition.py



**4. Operation:**





The webcam feed will open, and recognized faces will be labeled with their name and "Present" status.



Attendance is logged in a CSV file (e.g., 2025-05-04.csv) with columns for name and timestamp.



Press q to stop the program and close the webcam feed.

## **Usage:**





Ensure the webcam is working and the faces/ directory contains valid images.



Run the script using python face_recognition.py.



The system will:





Load known face encodings from the faces/ directory.



Capture and process the webcam feed to detect and recognize faces.



Display recognized names on the video feed.



Log attendance in a CSV file with the format: [name, HH-MM-SS].



To exit, press q in the video window.

## **Notes:**





The script currently loads two encodings for the same image (pareexit.jpg), which is redundant. Update the known_face_encoding and known_face_names lists to include unique individuals.



Ensure face images are clear and well-lit for accurate recognition.



The CSV file is created with the current date and remains open until the program exits. Avoid manually editing it during execution.



The video feed is resized to 25% of its original size for faster processing. Adjust the fx and fy parameters in cv2.resize if needed.

## **Troubleshooting:**





Webcam not working: Ensure the webcam is connected and accessible (try changing the cv2.VideoCapture(0) index if you have multiple cameras).



Face recognition errors: Verify that the face_recognition library is installed correctly and that face images are valid.



CSV file issues: Ensure write permissions in the project directory and check for file conflicts.

## **Contributing:**

Contributions are welcome! Please:





1. Fork the repository.



2. Create a new branch (git checkout -b feature-branch).



3. Make your changes and commit (git commit -m "Add feature").



4. Push to the branch (git push origin feature-branch).



5. Open a pull request.

## **License:**

This project is licensed under the MIT License. See the LICENSE file for details.
