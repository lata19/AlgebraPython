import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Smart Key")

# ---- FUNCTIONS ----
def ring():
    lbl_text.set("Zvoni zvono!")
    lbl_print.after(5000, text_reset)


def text_reset():
    lbl_text.set("")


def unlock_door():
    global btn_unlock_door_text
    if btn_unlock_door_text.get() == "Otključaj vrata":
        btn_unlock_door_text.set("Zaključaj vrata")
        lbl_text.set("Vrata su otključana")
        lbl_print.after(5000, text_reset)
    elif btn_unlock_door_text.get() == "Zaključaj vrata":
        btn_unlock_door_text.set("Otključaj vrata")
        lbl_text.set("Vrata su zaključana")
        lbl_print.after(5000, text_reset)


# ---- LOGIN ----
frm_login = ttk.Frame(root).grid(column=0, columnspan=4, row=0, rowspan=2)

lbl_frm_login = ttk.LabelFrame(frm_login, text="Prijava")
lbl_frm_login.columnconfigure(0, weight=1)
lbl_frm_login.columnconfigure(1, weight=3)
lbl_frm_login.grid(column=0, columnspan=4, row=0, rowspan=2, padx=10, pady=10)

# ---- USERNAME ----
lbl_username = ttk.Label(lbl_frm_login, text="Korisničko ime:")
lbl_username.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

entry_username = ttk.Entry(lbl_frm_login)
entry_username.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# ---- PASSWORD ----
lbl_password = ttk.Label(lbl_frm_login, text="Lozinka:")
lbl_password.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

entry_password = ttk.Entry(lbl_frm_login)
entry_password.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# ---- BUTTONS ----
frm_buttons = ttk.Frame(root).grid(column=0, columnspan=4, row=3)

btn_ring = ttk.Button(frm_buttons, text="Pozovni", command=ring)
btn_ring.grid(column=0, row=3, padx=10, pady=5)
# btn_ring.bind("<Button>", ring)

btn_unlock_door_text = tk.StringVar()
btn_unlock_door_text.set("Otključaj vrata")
btn_unlock_door = ttk.Button(
    frm_buttons, textvariable=btn_unlock_door_text, command=unlock_door
)
btn_unlock_door.grid(column=2, row=3, pady=5)
# btn_unlock_door.bind("<Button>", unlock_door)

frm_print = ttk.Frame(root).grid(column=0, columnspan=4, row=4)

lbl_text = tk.StringVar()
lbl_text.set("")

lbl_print = ttk.Label(frm_print, textvariable=lbl_text, justify="center")
lbl_print.grid(column=0, columnspan=4, row=4)

root.mainloop()
