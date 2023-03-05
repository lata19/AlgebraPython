from PIL import Image, ImageDraw

fotografija = Image.open("8.Photo/Fotografije/Algebra_campus.jpg")

fotografija_crtanje = ImageDraw.Draw(fotografija)

fotografija_crtanje.rectangle((800, 500, 3400, 2200), fill=None, outline="red", width=5)


fotografija_crtanje.ellipse((2500, 610, 3330, 1250), fill=None, outline="blue", width=5)

fotografija.show()