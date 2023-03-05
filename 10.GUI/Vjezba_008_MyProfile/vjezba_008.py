import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Moj profil - Nikola Latinčić")
# root.geometry("800x600")
font = "Lucida Console"
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


photo = Image.open("10.GUI/Vjezba_008_MyProfile/Latincic_Nikola.jpg").resize((200, 200))
profile_photo = ImageTk.PhotoImage(photo)

# Profilna i osnovne informacije
frm_intro = tk.Frame(root).grid(column=0, columnspan=2, row=0)


lbl_profile_photo = tk.Label(frm_intro, image=profile_photo).grid(
    column=0, row=0, padx=5, pady=5
)
lbl_personal_data = tk.Label(
    frm_intro,
    text="Nikola Latinčić\n06.11.1997.\nAleja pomoraca 17, Zagreb\nMagistar inženjer prometa",
    font=(font, 16),
    justify="left",
    anchor="nw",
).grid(column=0, row=1, padx=15, pady=15)

# Edukacija i iskustvo
frm_education = tk.Frame(root).grid(column=0, columnspan=2, padx=5, pady=5)
# FRAME Srednja škola
frm_high_school = tk.Frame(frm_education).grid(column=0, columnspan=2, padx=10, pady=10)
lbl_high_school_name = tk.Label(
    frm_high_school,
    text="Tehnička škola Zagreb, Palmotićeva 84, Zagreb",
    anchor="nw",
    justify="left",
    font=(font, 16),
).grid(column=0, row=2)
lbl_high_school_title = tk.Label(
    frm_high_school,
    text="Tehničar za računalstvo",
    anchor="nw",
    justify="left",
    font=(font, 14),
).grid(column=0, row=3)
lbl_high_school_description = tk.Label(
    frm_high_school,
    text="Programiranje u programskom jeziku C, sastavljanje i rastavljanje računala",
    anchor="nw",
    justify="left",
    font=(font, 12),
).grid(column=0, row=4)

# FRAME Fakultet
frm_faculty = tk.Frame(frm_education).grid(column=0, padx=10, pady=10)
lbl_faculty1_name = tk.Label(
    frm_faculty,
    text="Fakultet prometnih znanosti, Vukelićeva 4, Zagreb",
    anchor="nw",
    justify="left",
    font=(font, 16),
).grid(column=0)
lbl_faculty1_title = tk.Label(
    frm_faculty,
    text="Sveučilišni prvostupnik inženjer prometa\nuniv. bacc. ing. traff.",
    anchor="nw",
    justify="left",
    font=(font, 14),
).grid(column=0)
lbl_faculty1_description = tk.Label(
    frm_faculty,
    text="Diplomski rad: Opravdanost izvedbe kružnog raskrižja sa osnova sigurnosti prometa",
    anchor="nw",
    justify="left",
    font=(font, 12),
).grid(column=0)

root.mainloop()
