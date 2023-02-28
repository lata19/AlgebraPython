import tkinter as tk

def click():
    print("Gumb je kliknut")

root = tk.Tk()

root.title("Algebra - Python programer")
root.geometry("600x400")

# button = tk.Button(root, text="Gumb")
# button.pack()

button_with_click = tk.Button(root, text="Klikni me!", command=click).pack(padx=10, pady=10)


root.mainloop()

