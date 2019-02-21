import employee as em
import cv2
import pyttsx3


emp_id,emp_name=em.employee_entry()

path=em.dir_create(emp_id)

cap=cv2.VideoCapture(0)

count = 1
while True:
    ret,test_img=cap.read()
    if not ret :
        continue
    cv2.imwrite(path+"\\"+"%d.jpg" % count, test_img)     # save frame as JPG file
    count += 1
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    if cv2.waitKey(10) == ord('q') or count == 50:#wait until 'q' key is pressed
        engine = pyttsx3.init()
        engine.say("thank you we will train my system please wait.")
        engine.runAndWait()
        cap.release()
        cv2.destroyAllWindows
        break

