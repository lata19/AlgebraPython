"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              OpenCV Library
                    DNN Deep Neural Networks
                    Repositorij za build modela: https://github.com/opencv/opencv/tree/master/modules/dnn/misc
                    Teorija i primjer: Deep Neural Networks (dnn module)
"""

import os
import cv2
import numpy

if not os.path.exists("8.Photo//OpenCV/Rezultat"):
    os.makedirs("8.Photo//OpenCV/Rezultat")

putanja_fotografije = "8.Photo/Fotografije/Algebra_greyp.jpg"
fotografija = cv2.imread(putanja_fotografije)

model = cv2.dnn.readNetFromCaffe(
    "8.Photo/OpenCV/deploy.prototxt", "8.Photo/OpenCV/weights.caffemodel"
)


resizana = cv2.resize(fotografija, (300, 300))
blob_slika = cv2.dnn.blobFromImage(resizana, 1.0, (300, 300), (104.0, 177.0, 123.0))

model.setInput(blob_slika)
detektirana_lica = model.forward()


# Preuzmimo prve dvije vrijednosti iz shape liste vezane uz sliku: sirinu i visinu i pohtranimo ih u tuple
(height, width) = fotografija.shape[:2]

# Sada kada imamo prepoznavanje, prodimo kroz listu i oznacimo ih na fotografiji
broj_lica = 0
for i in range(0, detektirana_lica.shape[2]):
    okvir = detektirana_lica[0, 0, i, 3:7] * numpy.array([width, height, width, height])
    (startX, startY, endX, endY) = okvir.astype("int")

    # Broj prepoznatih lica ja jako velik. Pomocu postotka kolika je vjerojatnost da je sekcija slike
    # u stvari prepoznato lice, mozemo se "igrati" s prikazom pravokutnika.
    # Iz ovog primjer: ako je vjerojatnost veca od 14%, onda iscrtaj okvir na slici
    vjerojatnost = detektirana_lica[0, 0, i, 2]
    if vjerojatnost > 0.14:
        cv2.rectangle(fotografija, (startX, startY), (endX, endY), (0, 255, 0), 2)
        broj_lica += 1


# Dobivenu fotografiju mozemo pohraniti na disk
cv2.imwrite("8.Photo/OpenCV/" + fotografija, fotografija)

# A mozemo i prikazati u zasebnom okviru uz dodatak "cekanja" da se okvir ne bi odmah zatvorio
cv2.imshow("Pronadena lica", fotografija)
cv2.waitKey()

# Eventualno mozemo dodati poruku s brojem prepozntih lica
print(f"Prepoznavanje lica je zavrseno. Pronadeno je {broj_lica} lica.")