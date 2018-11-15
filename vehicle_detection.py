import time
import numpy as np
import cv2
import time
#num = 0
#def live(video_src):
cascade_src = 'cars.xml'

    # video_src = 'dataset/video1.avi'

def TakeSnapshotAndSave(video_src):
        cap = cv2.VideoCapture(video_src)
        car_cascade = cv2.CascadeClassifier(cascade_src)
        #num = 0


        #while num < 10:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

        x = 0
        y = 20
        text_color = (0, 255, 0)
        #while num < 10:


        num = 0
        time.sleep(5)
        cv2.imwrite('opencv' + str(num) + '.jpg', frame)
        return num

        #img = 'opencv' + str(num) + '.jpg'

        #return img







       # return num

        cap.release()
        cv2.destroyAllWindows()

    ##   TakeSnapshotAndSave()

    #return num