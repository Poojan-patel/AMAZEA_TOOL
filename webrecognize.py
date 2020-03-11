import cv2
import sys 
import copy
import time
import os
import re
import face_recognition

faceCascade = cv2.CascadeClassifier(sys.argv[1])
known_images = [os.path.join(sys.argv[2], f) for f in os.listdir(sys.argv[2]) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]
known_schemas = [face_recognition.load_image_file(i) for i in known_images]
known_encodings = [face_recognition.face_encodings(i) for i in known_schemas]

flag = False
frame = 5
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
#webcam.set(cv2.cv.CV_CAP_PROP_FPS, 10)
start = time.time()
#while (time.time() - start < 200):
while time.time() - start < 20:
    flag_run = True
    #print('hey')
    try:
        #global frame
        check, frame = webcam.read()
        frame2 = copy.copy(frame)
        #print(check) #prints true as long as the webcam is running
        #print(frame) #prints matrix values of each framecd 
        cv2.imshow("Face Recognition", frame)
        cv2.imwrite(filename="temp.jpg", img=frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(10, 10),
            #flags=cv2.CV_HAAR_SCALE_IMAGE
        )
        unknown_picture = face_recognition.load_image_file('temp.jpg',mode="RGB")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)

        if(len(unknown_face_encoding) != 0):
            results = face_recognition.compare_faces(known_encodings[0], unknown_face_encoding[0])

            for i in range(len(results)):
                if(results[i] == True):
                    print("Found: " + (re.split("['/','.']",known_images[i])[-2]))
                    flag_run = False
                    break
        #print(faces)

    # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (255, 255, 255), 3)
        cv2.imshow('Face Recognition', frame2)

        key = cv2.waitKey(10)
        if key == ord('s'):
            #global flag
            flag = True 
            webcam.release()
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            name = input("Enter Your Name:")+'.jpg'
            cv2.imwrite(filename=name, img=frame)
            

            img_new = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1000)
            print("Processing image...")
            img_ = cv2.imread(name, cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
        
            break
        elif (key == ord('q') or flag_run == False):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
if(flag == False and flag_run == True):
    webcam.release()
    cv2.waitKey(1650)
    cv2.destroyAllWindows()
    name = input("Enter Your Name:")+'.jpg'
    cv2.imwrite(filename=name, img=frame)

    