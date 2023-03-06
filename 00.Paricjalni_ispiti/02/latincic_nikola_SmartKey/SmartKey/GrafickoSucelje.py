import tkinter as tk

root = tk.Tk()
root.title("Smart Key")
font = "Aerial 11"


def ring():
    frm_pin.grid_forget()
    frm_message = tk.Frame(frm_buttons)
    frm_message.grid(column=4, row=4)

    lbl_message = tk.Label(
        frm_message, text="Zvono aktivirano!\nUskoro će netko doći i otvoriti vrata"
    )
    lbl_message.grid(column=6, row=0)


def unlock():
    frm_pin.grid(column=0, columnspan=10, row=3, rowspan=5, padx=10, pady=10)
    lbl_pin = tk.Label(frm_pin, text="PIN panel", font=font)
    z = 1
    for i in range(3):
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)
        for j in range(3):
            btn = tk.Button(
                frm_pin,
                width=7,
                height=2,
                bg="white",
                fg="black",
                relief="flat",
                text=z,
            )
            btn.grid(column=j, row=4 + i, padx=5, pady=5)
            z += 1

    button_zero = tk.Button(
        frm_pin, width=7, height=2, bg="white", fg="black", relief="flat", text="0"
    )
    button_zero.grid(column=1, row=7, padx=5, pady=5)
    button_clear = tk.Button(
        frm_pin, width=7, height=2, bg="white", fg="black", relief="flat", text="C"
    )
    button_clear.grid(column=2, row=7, padx=5, pady=5)

    frm_message = tk.Frame(frm_pin)
    frm_message.grid(column=4, row=4)

    lbl_message = tk.Label(frm_message, text="Status i poruke")
    lbl_message.grid(column=6, row=0)


# ---- FRAMES ----
# FRAME 1
frm_buttons = tk.Frame(root).grid(
    column=0, columnspan=10, row=0, rowspan=2, padx=10, pady=10
)

btn_ring = tk.Button(frm_buttons, text="Pozvoni", command=ring)
btn_ring.grid(column=0, row=0, padx=10, pady=10, sticky=tk.E)

btn_unlock = tk.Button(
    frm_buttons,
    text="Otkljucaj",
    command=unlock,
)
btn_unlock.grid(column=7, row=0, padx=10, pady=10, sticky=tk.W)

# FRAME 2
frm_pin = tk.Frame(root)
frm_pin.grid(column=0, columnspan=10, row=3, rowspan=5, padx=10, pady=10)

# FRAME 3
frm_admin_access = tk.Frame(root).grid(
    column=0, columnspan=10, row=8, rowspan=5, padx=10, pady=10
)

root.mainloop()
