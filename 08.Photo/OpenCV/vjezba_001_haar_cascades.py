import cv2


lica_haar_cascade = cv2.CascadeClassifier("8.Photo/OpenCV/haarcascade_frontalface_default.xml")

fotografija = cv2.imread("8.Photo/Fotografije/Algebra_greyp.jpg")

cb_fotografija = cv2.cvtColor(fotografija, cv2.COLOR_BGR2GRAY)

prepoznata_lica = lica_haar_cascade.detectMultiScale(cb_fotografija, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

# print(f"Pronašao sam {len(prepoznata_lica)}")

for pravokutnik in prepoznata_lica:
    x, y, w, h = pravokutnik
    cv2.rectangle(fotografija, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Pronadena lica", fotografija)
cv2.waitKey(0)