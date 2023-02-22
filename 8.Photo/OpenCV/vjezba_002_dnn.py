import os
import cv2
import numpy

if not os.path.exists("8.Photo/OpenCV/Rezultat"):
    os.makedirs("8.Photo/OpenCV/Rezultat")

putanja_fotografije = "8.Photo/Fotografije/Algebra_greyp.jpg"
fotografija = cv2.imread(putanja_fotografije)

model = cv2.dnn.readNetFromCaffe("8.Photo/OpenCV/deploy.prototxt", "8.Photo/OpenCV/weights.caffemodel")

resizana = cv2.resize(fotografija, (300, 300))
blob_slika = cv2.dnn.blobFromImage(resizana, 1.0, (300, 300), (104.0, 177.0, 123.0))

model.setInput(blob_slika)
detektirana_lica = model.forward()