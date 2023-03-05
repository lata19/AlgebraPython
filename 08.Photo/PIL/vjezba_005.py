from PIL import Image

logo_fotografija = Image.open("8.Photo/Fotografije/Python_logo_and_wordmark.png")
kampus_fotografija = Image.open("8.Photo/Fotografije/Algebra_campus.jpg")

print(logo_fotografija.size)
print(kampus_fotografija.size)

kampus_fotografija.paste(logo_fotografija, (500,300))

kampus_fotografija.show()