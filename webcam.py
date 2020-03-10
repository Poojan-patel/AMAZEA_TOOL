import cv2
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    flag = False
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10),
        #flags=cv2.CV_HAAR_SCALE_IMAGE
    )
    print(faces)

    # Draw a rectangle around the faces
    for (x, y, w, h),i in zip(faces,faces):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 3)
        if(len(i) > 0):
            flag = True
            break

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()