from PIL import Image

putanja_fotografije = "8.Photo/Fotografije/Algebra_campus.jpg"

fotografija = Image.open(putanja_fotografije)

fotografija_CB = fotografija.convert("L")

fotografija_CB.show()