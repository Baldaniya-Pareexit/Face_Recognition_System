import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces
pareexit_image = face_recognition.load_image_file("faces/pareexit.jpg")
pareexit_encoding = face_recognition.face_encoding(pareexit_image)[0]

img2 = face_recognition.load_image_file("faces/pareexit.jpg")
img2_encoding = face_recognition.face_encoding(img2)[0]

known_face_encoding = [pareexit_encoding, img2_encoding]
known_face_names = ["pareexit", "Image2"]

students = known_face_names.copy()

face_locations = []
face_encodings = []

# get the current date and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encoding(rgb_small_frame, face_locations)

    for face_encodings in face_encodings:
        matches = face_recognition.compare_faces(known_face_encoding, face_encodings)
        face_distance = face_recognition.face_distance(known_face_encoding, face_encodings)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

    # add the text if the person is present
    if name in known_face_names:
        font = cv2.FONT_HERSHEY_TRIPLEX
        bottomLeftCornerOfText = (10,100)
        fontScale = 1.5
        fontColor = (0, 255, 0)
        thickness = 2
        lyneType = 2
        cv2.putText(frame, name + "Present", bottomLeftCornerOfText, fontScale, fontColor, thickness, lyneType)

        if name in students:
            students.remove(name)
            current_time = now.strftime("%H-%M-%S")
            lnwriter.writerow([name, current_time])

    cv2.imshow("Attendence", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()