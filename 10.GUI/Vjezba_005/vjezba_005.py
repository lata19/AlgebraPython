import tkinter as tk

unesena_slova = ""

# handle_NekaAkcija
# on_NekaAkcija

def on_keypress(event):
    print(event.char)
    global unesena_slova
    unesena_slova += str(event.char)
    label_text_var.set(unesena_slova)


root = tk.Tk()
root.title("Algebra - Python programer")
root.geometry("800x600")

label_text_var = tk.StringVar()
label_text_var.set("Ovo je mjesto gdje ce se prikazivati unesena slova")

label_naslov = tk.Label(root, text="Key event", font=("Segoe UI", 18))
label_naslov.grid(column=0, row=0)


label_ispis = tk.Label(root, textvariable=label_text_var, font=("Segoe UI", 25), fg="red")
label_ispis.grid(column=0, row=1)

root.bind("<Key>", on_keypress)


root.mainloop()