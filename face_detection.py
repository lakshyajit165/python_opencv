import cv2

detect = cv2.CascadeClassifier('./venv/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# = cv2.VideoCapture("https://pixel.nymag.com/imgs/daily/vulture/2018/02/01/01-tom-cruise.w700.h700.jpg")
cam = cv2.VideoCapture("https://ichef.bbci.co.uk/news/660/cpsprodpb/1453F/production/_101236238_avengers2.jpg")

check, img = cam.read()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = detect.detectMultiScale(gray, 1.20, 5)

for x,y,w,h in face:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('Face', img)
cv2.waitKey(0)

cam.release()
cv2.destroyAllWindows()