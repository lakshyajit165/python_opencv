import cv2

#create CascadeClassifier Object
face_cascade = cv2.CascadeClassifier('./venv/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#Reading the image as it is
img = cv2.imread('Tom.jpg')

#Reading the image as grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

#resized = cv2.resize(img, int(img.shape[1])/2, int(img.shape[0])/2)

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()