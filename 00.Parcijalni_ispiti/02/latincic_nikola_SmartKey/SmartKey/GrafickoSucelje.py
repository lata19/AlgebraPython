from tkinter import *
from BazaPodataka import *

insertion = ""


class SmartKey(Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Key")

        self.active_var = BooleanVar()

        # FRAME 1
        self.frm_buttons = Frame(self)
        self.frm_buttons.grid(columnspan=10, rowspan=3)

        self.lbl_buttons_frm = Label(self.frm_buttons, text="Panel s gumbima")
        self.lbl_buttons_frm.grid(column=4, columnspan=2, row=0)

        self.btn_ring = Button(self.frm_buttons, text="Pozvoni", command=self.ring)
        self.btn_ring.grid(column=2, columnspan=2, row=2, padx=10, pady=10, ipadx=20)

        self.btn_unlock = Button(
            self.frm_buttons, text="Otkljucaj", command=self.unlock
        )
        self.btn_unlock.grid(column=7, columnspan=2, row=2, padx=10, pady=10, ipadx=20)

        self.frm_message = Frame(self)

        # FRAME 2
        self.frm_pin = Frame(self)

        self.lbl_message2 = Label(self.frm_pin, text="Uspjesna prijava")
        self.lbl_message3 = Label(self.frm_pin, text="Pogresan PIN.\nPozvonite!")

        # FRAME 3
        self.frm_admin = Frame(self)

    def ring(self):
        self.frm_pin.grid_forget()
        self.frm_admin.grid_forget()
        self.frm_message.grid(columnspan=10, row=3, padx=10)

        self.lbl_ring_message = Label(
            self.frm_message,
            text="Zvono aktivirano!\nUskoro će netko doći i otvoriti vrata",
        )
        self.lbl_ring_message.grid(column=5, row=0, ipadx=20)

    def unlock(self):
        self.frm_message.grid_forget()
        self.frm_pin.grid(columnspan=10, row=3, rowspan=6)

        self.lbl_pin_frm = Label(self.frm_pin, text="PIN panel")
        self.lbl_pin_frm.grid(column=4, columnspan=2, row=0)

        # ENTRY FRAMES
        # TODO
        # Napraviti 4 frame u koje ce se upisivati odabrani brojevi
        self.pin_entry = Entry(self.frm_pin)
        self.pin_entry.grid(column=0, columnspan=3, row=1, pady=10)

        # BUTTON NUMBERS
        self.btn_1 = Button(
            self.frm_pin, text=1, padx=20, pady=10, command=lambda: self.number_click(1)
        )
        self.btn_1.grid(column=0, row=4)
        self.btn_2 = Button(
            self.frm_pin, text=2, padx=20, pady=10, command=lambda: self.number_click(2)
        )
        self.btn_2.grid(column=1, row=4)
        self.btn_3 = Button(
            self.frm_pin, text=3, padx=20, pady=10, command=lambda: self.number_click(3)
        )
        self.btn_3.grid(column=2, row=4)

        self.btn_4 = Button(
            self.frm_pin, text=4, padx=20, pady=10, command=lambda: self.number_click(4)
        )
        self.btn_4.grid(column=0, row=3)
        self.btn_5 = Button(
            self.frm_pin, text=5, padx=20, pady=10, command=lambda: self.number_click(5)
        )
        self.btn_5.grid(column=1, row=3)
        self.btn_6 = Button(
            self.frm_pin, text=6, padx=20, pady=10, command=lambda: self.number_click(6)
        )
        self.btn_6.grid(column=2, row=3)

        self.btn_7 = Button(
            self.frm_pin, text=7, padx=20, pady=10, command=lambda: self.number_click(7)
        )
        self.btn_7.grid(column=0, row=2)
        self.btn_8 = Button(
            self.frm_pin, text=8, padx=20, pady=10, command=lambda: self.number_click(8)
        )
        self.btn_8.grid(column=1, row=2)
        self.btn_9 = Button(
            self.frm_pin, text=9, padx=20, pady=10, command=lambda: self.number_click(9)
        )
        self.btn_9.grid(column=2, row=2)

        self.btn_del = Button(
            self.frm_pin, text="DEL", padx=13, pady=10, command=self.delete_number
        )
        self.btn_del.grid(column=0, row=5)

        self.btn_0 = Button(
            self.frm_pin, text=0, padx=20, pady=10, command=lambda: self.number_click(0)
        )
        self.btn_0.grid(column=1, row=5)

        self.btn_c = Button(
            self.frm_pin, text="C", padx=19, pady=10, command=self.clear_insertion
        )
        self.btn_c.grid(column=2, row=5)

        self.lbl_message = Label(self.frm_pin, text="Status i poruke")
        self.lbl_message.grid(column=6, row=1, padx=10, sticky=N)

    def number_click(self, number):
        global insertion
        insertion += str(number)
        self.pin_entry.delete(0, END)
        self.pin_entry.insert(0, insertion)
        if len(self.pin_entry.get()) == 4:
            self.user_check()
            insertion = ""
            self.pin_entry.delete(0, END)

    def delete_number(self):
        global insertion
        insertion = insertion.rstrip(insertion[-1])
        self.pin_entry.delete(0, END)
        self.pin_entry.insert(0, insertion)

    def clear_insertion(self):
        global insertion
        insertion = ""
        self.pin_entry.delete(0, END)

    def user_check(self):
        session = create_engine()
        access = pin_access(session, self.pin_entry.get())
        if access:
            first_name, last_name, access = get_user_by_pin(
                session, self.pin_entry.get()
            )
            if first_name == "Admin" and last_name == "Admin":
                self.admin_frame()
            else:
                self.lbl_message3.grid_forget()
                self.lbl_message2.grid(column=6, row=3, padx=10)
        else:
            self.lbl_message2.grid_forget()
            self.lbl_message3.grid(column=6, row=3, padx=10)

    def admin_frame(self):
        self.lbl_message3.grid_forget()
        self.lbl_message2.grid_forget()
        self.frm_admin.grid(columnspan=10, row=9, rowspan=6)
        self.lbl_admin = Label(
            self.frm_admin, text="Upravljanje dodijeljenim ključevima"
        )
        self.lbl_admin.grid(column=4, columnspan=2, row=0, padx=10, pady=10)

        self.lbl_list_of_users = Label(self.frm_admin, text="Popis aktivnih korisnika")
        self.lbl_list_of_users.grid(column=0, columnspan=3, row=1, pady=10)
        session = create_engine()
        family = get_all_family_members(session)

        # TODO
        # napraviti da se klikom na ime clana obitelji upisu njegovi podaci u entries

        i = 2
        for user in family:
            self.btn_users = Button(
                self.frm_admin,
                text=f"{user.first_name} {user.last_name}",
                width=12,
                command=lambda: self.fill_fields(
                    user.first_name, user.last_name, user.pin, user.active
                ),
            )
            self.btn_users.grid(column=0, columnspan=3, row=i, pady=5)
            i += 1
        # all_members = []
        # member = []
        # i = 2
        # for user in family:
        #     first_name = user.first_name
        #     last_name = user.last_name
        #     pin = user.pin
        #     active = user.active

        #     member[0] = first_name
        #     member[1] = last_name
        #     member[2] = pin
        #     member[3] = active
        #     all_members.append(member)

        # for member in all_members:
        #     self.btn_users = Button(
        #         self.frm_admin,
        #         text=f"{member[0]} {member[1]}",
        #         width=12,
        #         command=lambda: self.fill_fields(
        #             member[0], member[1], member[2], member[3]
        #         ),
        #     )
        #     self.btn_users.grid(column=0, columnspan=3, row=i, pady=5)
        #     i += 1

        self.lbl_first_name = Label(self.frm_admin, text="Ime")
        self.lbl_first_name.grid(column=4, row=2)
        self.first_name_entry = Entry(self.frm_admin)
        self.first_name_entry.grid(column=5, columnspan=2, row=2)

        self.lbl_last_name = Label(self.frm_admin, text="Prezime")
        self.lbl_last_name.grid(column=4, row=3)
        self.last_name_entry = Entry(self.frm_admin)
        self.last_name_entry.grid(column=5, columnspan=2, row=3)

        self.lbl_pin = Label(self.frm_admin, text="PIN (4 broja)")
        self.lbl_pin.grid(column=4, row=4)
        self.pin_edit_entry = Entry(self.frm_admin)
        self.pin_edit_entry.grid(column=5, columnspan=2, row=4)

        self.lbl_active = Label(self.frm_admin, text="Aktivan")
        self.lbl_active.grid(column=4, row=5)
        self.active_cb = Checkbutton(self.frm_admin, variable=self.active_var)
        self.active_cb.grid(column=5, row=5)

        self.btn_save = Button(
            self.frm_admin,
            text="Spremi",
            command=lambda: self.save(
                self.first_name_entry.get(),
                self.last_name_entry.get(),
                self.pin_edit_entry.get(),
                self.active_var.get(),
            ),
        )
        self.btn_save.grid(column=4, row=6, padx=10)
        self.btn_cancel = Button(self.frm_admin, text="Odustani", command=self.cancel)
        self.btn_cancel.grid(column=5, row=6, padx=10)
        self.btn_delete = Button(
            self.frm_admin,
            text="Izbrisi",
            command=lambda: self.delete(
                self.first_name_entry.get(),
                self.last_name_entry.get(),
                self.pin_edit_entry.get(),
            ),
        )
        self.btn_delete.grid(column=6, row=6, padx=10)

    def fill_fileds(self, first_name, last_name, pin, active):
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.pin_edit_entry.delete(0, END)
        self.active_var.set(False)

        self.first_name_entry.insert(0, first_name)
        self.last_name_entry.insert(0, last_name)
        self.pin_edit_entry.insert(0, pin)
        self.active_var.set(active)
        pass

    def save(self, first_name, last_name, pin, active):
        session = create_engine()
        add_person(session, first_name, last_name, pin, active)
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.pin_edit_entry.delete(0, END)
        self.active_var.set(False)

    def cancel(self):
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.pin_edit_entry.delete(0, END)
        self.active_var.set(False)

    def delete(self, first_name, last_name, pin):
        session = create_engine()
        delete_user(session, first_name, last_name, pin)


root = SmartKey()

root.mainloop()
