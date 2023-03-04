import tkinter as tk

root = tk.Tk()
root.title("Algebra - Python programer")
root.geometry("600x400")

# kreirati cemo polje od 3 x 3 elementa
for i in range(3):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=75)

    for j in range(3):
        frame = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=15, pady=15)
        label = tk.Label(frame, text=f"Red {i}\nKolona {j}")
        label.pack(padx=15, pady=15)

root.mainloop()