from PIL import Image

putanja_fotografije = "8.Photo/Fotografije/Algebra_campus.jpg"

fotografija = Image.open(putanja_fotografije)

print(f"Format fotografije: {fotografija.format}")
print(f"Mod fotografije: {fotografija.mode}")
print(f"Dimenzije fotografije: {fotografija.size[0]} x {fotografija.size[1]}")

fotografija.show()