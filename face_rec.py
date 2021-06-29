# import cv2
#
# classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
# while True:
#     success, img = cap.read()
#     if success:
#         faces = classifier.detectMultiScale(img)
#         for face in faces:
#             x,y,w,h = face
#             img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
#             cv2.imshow("Video", img)
#     if cv2.waitKey(32) & 0xFF == ord('q'):
#         break

###########################################################################
# All the imports go here
# import time
#
# import numpy as np
# import cv2
#
# # Initializing the face and eye cascade classifiers from xml files
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#
# # Variable store execution state
# first_read = True
# success = False
# # Starting the video capture
# cap = cv2.VideoCapture(0)
# cap.set(3,1080)
# cap.set(4,1080)
# cap.set(10,100)
#
# #
# # def countdown(t):
# #     while t:
# #         mins, secs = divmod(t, 60)
# #         timer = '{:02d}:{:02d}'.format(mins, secs)
# #         # print(timer, end="\r")
# #         # time.sleep(1)
# #         t -= 1
#
# ret, img = cap.read()
# count = 0
# start = 0
# end = 0
# while (ret):
#     ret, img = cap.read()
#     # Coverting the recorded image to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Applying filter to remove impurities
#     gray = cv2.bilateralFilter(gray, 5, 1, 1)
#
#     # Detecting the face for region of image to be fed to eye classifier
#     faces = face_cascade.detectMultiScale(gray, 1.3, 4, minSize=(50, 50))
#     if (len(faces) > 0):
#         for (x, y, w, h) in faces:
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#             # roi_face is face which is input to eye classifier
#             roi_face = gray[y:y + h, x:x + w]
#             roi_face_clr = img[y:y + h, x:x + w]
#             eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 4, minSize=(5, 5))
#
#             # Examining the length of eyes object for eyes
#             if (len(eyes) >= 2):
#
#                 if(success):
#                     if(start > 25 and count < 2):
#                         cv2.putText(img, "Fake", (70, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)
#                     else:
#                         success = False
#                 else:
#
#                     if count > 2:
#                         cv2.putText(img, "You are Live, press q", (70, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
#
#
#                     # Check if program is running for detection
#                     elif (first_read):
#                         cv2.putText(img, "Eye detected press s ", (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0),
#                                     2)
#                     else:
#                         if(not success):
#                             cv2.putText(img, "Eyes open!", (70, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
#                             if(True):
#                                 end = time.process_time()
#                             if((end - start) > 20):
#                                 print("Time up")
#                                 cv2.putText(img, "Fake", (70, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)
#
#                         # countdown(5)
#                         # cv2.putText(img, "Fake", (70, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)
#
#
#
#             else:
#                 if (first_read):
#                     # To ensure if the eyes are present before starting
#                     cv2.putText(img, "Eye not detected", (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
#                 else:
#                     # This will print on console and restart the algorithm
#                     print("Blink detected--------------")
#                     count = count +1
#                     cv2.waitKey(500)
#                     first_read = True
#
#
#     else:
#         cv2.putText(img, "No face detected", (100, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
#
#     # Controlling the algorithm with keys
#     cv2.imshow('img', img)
#     a = cv2.waitKey(1)
#     if (a == ord('q')):
#         break
#     elif (a == ord('s') and first_read):
#         start = time.process_time()
#         success = True
#         # This will start the detection
#         first_read = False
#
# cap.release()
# cv2.destroyAllWindows()
#

#############################################################################################

# trial
import sys
import time

import numpy as np
import cv2

# Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# Variable store execution state
first_read = True
success = False
spoof = False
# Starting the video capture
cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,1080)
cap.set(10,100)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1

ret, img = cap.read()
count = 0
start = 0
end = 0
while (ret):
    ret, img = cap.read()
    # Coverting the recorded image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Applying filter to remove impurities
    gray = cv2.bilateralFilter(gray, 5, 1, 1)

    # Detecting the face for region of image to be fed to eye classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 4, minSize=(50, 50))
    if (len(faces) > 0):
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # roi_face is face which is input to eye classifier
            roi_face = gray[y:y + h, x:x + w]
            roi_face_clr = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 4, minSize=(5, 5))

            # Examining the length of eyes object for eyes
            if (len(eyes) >= 2):
                    if count > 2:
                        cv2.putText(img, "You are Live, press q", (x - 25, y - 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 5)
                    # Check if program is running for detection
                    elif (first_read):
                        cv2.putText(img, "Eye detected press s ", (x - 25, y - 25), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    else:
                        if(success):
                            cv2.putText(img, "Eyes open!", (x, y - 25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                            if(True):
                                end = time.process_time()
                            if (spoof):
                                countdown(5)
                                sys.exit("Spoofing Spotted")
                            if((end - start) > 30):
                                cv2.putText(img, "Fake", (x, y - 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 5)
                                print("Time up")
                                # first_read = False
                                spoof = True



            else:
                if (first_read):
                    # To ensure if the eyes are present before starting
                    cv2.putText(img, "Eye not detected", (x - 25, y - 25), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                else:
                    # This will print on console and restart the algorithm
                    print("Blink detected--------------")
                    count = count +1
                    cv2.waitKey(500)
                    first_read = True

    else:
        cv2.putText(img, "No face detected", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    # Controlling the algorithm with keys
    cv2.imshow('img', img)
    a = cv2.waitKey(1)
    if (a == ord('q')):
        break
    elif (a == ord('s') and first_read):
        start = time.process_time()
        success = True
        # This will start the detection
        first_read = False

cap.release()
cv2.destroyAllWindows()

