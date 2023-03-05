from PIL import Image

putanja_fotografije = "8.Photo/Fotografije/Algebra_campus.jpg"

fotografija = Image.open(putanja_fotografije)

lijevo = 500
gore = 500
desno = fotografija.size[0] - 500
dolje = fotografija.size[1] - 500


cropped_img = fotografija.crop((lijevo, gore, desno, dolje))

cropped_img.save("8.Photo/Fotografije/Algebra_campus_cropped.jpg", "JPEG")
cropped_img.save("8.Photo/Fotografije/Algebra_campus_cropped.png")
