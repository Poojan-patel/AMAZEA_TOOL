import cv2
import sys 
import copy
import time
import os
import re
import face_recognition

def function_for_face_reco(arg):
    faceCascade = cv2.CascadeClassifier(arg[1])
    known_images = [os.path.join(arg[2], f) for f in os.listdir(arg[2]) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]
    known_schemas = [face_recognition.load_image_file(i) for i in known_images]
    known_encodings = [face_recognition.face_encodings(i)[0] for i in known_schemas]

    flag = False
    dic = {}
    frame = 5
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    start = time.time()
    #while (time.time() - start < 200):
    while time.time() - start < 20:
        flag_run = True
        #print('hey')
        try:
            #global frame
            check, frame = webcam.read()
            frame2 = copy.copy(frame) 
            cv2.imshow("Face Recognition", frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(10, 10),
                #flags=cv2.CV_HAAR_SCALE_IMAGE
            )
            unknown_face_encoding = face_recognition.face_encodings(frame)

            if(len(unknown_face_encoding) != 0):
                results = face_recognition.compare_faces(known_encodings, unknown_face_encoding[0],tolerance=0.5)

                for i in range(len(results)):
                    if(results[i] == True):
                        x = re.split("['/','.']",known_images[i])[-2]
                        if x not in dic.keys():
                            dic[x]=0
                        else:
                            dic[x] +=1
                        #flag_run = False
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame2, (x, y), (x+w, y+h), (255, 255, 255), 3)
                cv2.putText(frame2, "Face", (x+w-50,y+h-10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,60), 2)
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
                flag = True
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
    total_detection = sum(dic.values())+1
    maxi = 0
    person = ""
    for i,j in dic.items():
        if(j/total_detection > maxi and j/total_detection):
            maxi = j/total_detection
            person = i
    webcam.release()
    cv2.waitKey(1650)
    cv2.destroyAllWindows()
    print(dic)
    if(maxi < 0.45 and len(dic.keys()) != 1):
        #name = input("Enter Your Name:")+'.jpg'
        #cv2.imwrite(filename=name, img=frame)
        return "No",frame
    else:
        return person,frame


if __name__ == "__main__":
    name,frame = function_for_face_reco(sys.argv)
    if(name == 'No'):
        name = './Known/'+input('Your Good Name:')+'.jpg'
        cv2.imwrite(filename=name, img=frame)
