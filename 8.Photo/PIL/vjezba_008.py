from PIL import Image, ImageFilter

fotografija = Image.open("8.Photo/Fotografije/Algebra_campus.jpg")

# fotografija.filter(ImageFilter.CONTOUR).show()
# fotografija.filter(ImageFilter.EDGE_ENHANCE).show()
# fotografija.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
# fotografija.filter(ImageFilter.EMBOSS).show()
# fotografija.filter(ImageFilter.FIND_EDGES).show()
# fotografija.filter(ImageFilter.SHARPEN).show()
# fotografija.filter(ImageFilter.SMOOTH).show()
# fotografija.filter(ImageFilter.SMOOTH_MORE).show()
# fotografija.filter(ImageFilter.BLUR).show()
# fotografija.filter(ImageFilter.BoxBlur(3)).show()
# fotografija.filter(ImageFilter.BoxBlur(10)).show()
# fotografija.filter(ImageFilter.DETAIL).show()
# fotografija.filter(ImageFilter.GaussianBlur(8)).show()
fotografija.filter(ImageFilter.MaxFilter()).show()
fotografija.filter(ImageFilter.MedianFilter()).show()
fotografija.filter(ImageFilter.MinFilter()).show()

