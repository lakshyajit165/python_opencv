import cv2

#colored image
img = cv2.imread('wallpaper.jpg',1)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Laptop", resized)

cv2.waitKey(2000)

cv2.destroyAllWindows()

