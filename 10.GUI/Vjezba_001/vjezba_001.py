import tkinter as tk

def click():
    print("Gumb je kliknut")

root = tk.Tk()

root.title("Algebra - Python programer")
root.geometry("600x400")

# button = tk.Button(root, text="Gumb")
# button.pack()

button_with_click = tk.Button(root, text="Klikni me!", command=click).pack(padx=10, pady=10)

image = tk.PhotoImage(file="8.Photo/Fotografije/python-logo.png").subsample(50)
button_image = tk.Button(root, text="Gumb sa slicicom", image=image, compound=tk.LEFT, relief=tk.GROOVE, command=click, state=tk.DISABLED)
button_image.pack(padx=10, pady=10)


root.mainloop()

