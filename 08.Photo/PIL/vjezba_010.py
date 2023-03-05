from PIL import Image, ImageEnhance

fotografija = Image.open("8.Photo/Fotografije/Algebra_campus.jpg")

# pojacivac_fotografija = ImageEnhance.Brightness(fotografija)
# pojacivac_fotografija.enhance(0.4).show()

# pojacivac_fotografija = ImageEnhance.Contrast(fotografija)
# pojacivac_fotografija.enhance(4).show()

# pojacivac_fotografija = ImageEnhance.Sharpness(fotografija)
# pojacivac_fotografija.enhance(20).show()

pojacivac_fotografija = ImageEnhance.Color(fotografija)
pojacivac_fotografija.enhance(6).show()