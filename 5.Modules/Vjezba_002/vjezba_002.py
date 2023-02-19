import datetime as dt
from dateutil import tz

# datum_korisnik = input("Upišite danasnji datum i vrijeme u formatu: dan. naziv_mjeseca godina. sati:minuta:sekunda - ")
# datum_korisnik = "14 February 2023. 18:52:23"
# datum_objekt = dt.datetime.strptime(datum_korisnik, "%d. %B %Y. %H:%M:%S")

# print(datum_korisnik)
# print(datum_objekt)

# print(datum_objekt.year)
# print(datum_objekt.month)

sadasnji_trenutak = dt.datetime.now()
novi_datum_objekt = dt.datetime.strptime("24. July 1975. 4:45:4", "%d. %B %Y. %H:%M:%S")

razlika = sadasnji_trenutak - novi_datum_objekt
print(razlika)

# zbroj = novi_datum_objekt + sadasnji_trenutak
# print(zbroj)

za_2_tjedna = sadasnji_trenutak + dt.timedelta(days=14, hours=14)
print(za_2_tjedna)

danas = dt.date.today()
jucer = danas - dt.timedelta(days=1)
sutra = danas + dt.timedelta(days=1)

print("Jucerasnji dan:", jucer)
print("Danasnji dan:", danas)
print("Sutrasnji dan:", sutra)



# datum = dt.date(2023, 2, 20)
# print(datum)

# Vremenske zone
tz_zg = tz.gettz("Europe/Zagreb")
termin_zg = dt.datetime(2023, 1, 1, tzinfo=tz_zg)

tz_ny = tz.gettz("America/New_York")
termin_ny = termin_zg.astimezone(tz_ny)

tz_tk = tz.gettz("Asia/Tokyo")
termin_tk = termin_zg.astimezone(tz_tk)


print(f"Termin u Zagrebu počinje u: {termin_zg.strftime('%A %d.%m.%Y. %H:%M')}")
print(f"Termin u New Yorku počinje u: {termin_ny.strftime('%A %d.%m.%Y. %H:%M')}")
print(f"Termin u Tokyu počinje u: {termin_tk.strftime('%A %d.%m.%Y. %H:%M')}")



tz_tk = tz.gettz("Asia/Tokyo")
termin_og_tk = dt.datetime(2021, 7, 23, 20, tzinfo=tz_tk)

tz_zg = tz.gettz("Europe/Zagreb")
termin_og_zg = termin_og_tk.astimezone(tz_zg)

tz_ny = tz.gettz("America/New_York")
termin_og_ny = termin_og_tk.astimezone(tz_ny)



print(f"Olimpijske igre u Tokyu počinje u: {termin_og_tk.strftime('%A %d.%m.%Y. %H:%M')}")
print(f"Olimpijske igre u Tokyu u Zagrebu počinje u: {termin_og_zg.strftime('%A %d.%m.%Y. %H:%M')}")
print(f"Olimpijske igre u Tokyu u New Yorku počinje u: {termin_og_ny.strftime('%A %d.%m.%Y. %H:%M')}")
