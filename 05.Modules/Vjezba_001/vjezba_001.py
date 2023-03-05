import datetime as dt
import locale

# Danasnji datum
danasnji_dan = dt.date.today()
print(f"Danasnji dan je: {danasnji_dan}")
# YYYY-MM-DD

# Sadašnji trenutak
sadasnji_trenutak = dt.datetime.now()
print(f"\nSadašnji trenutak je: {sadasnji_trenutak}")
# YYYY-MM-DD HH:MM:SS.MS

# Dan u tjednu
dan_u_tjednu = dt.date.weekday(danasnji_dan)
print(f"Danas je {dan_u_tjednu}. dan u tjednu")
print(f"ISPRAVNO: Danas je {dan_u_tjednu + 1}. dan u tjednu")

if dan_u_tjednu == 0:
    print(f"Danas je ponedjeljak, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 1:
    print(f"Danas je utorak, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 2:
    print(f"Danas je srijeda, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 3:
    print(f"Danas je četvrtak, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 4:
    print(f"Danas je petak, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 5:
    print(f"Danas je subota, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 6:
    print(f"Danas je nedjelja, {dan_u_tjednu+1}. dan u tjednu")



print("\nDan u tjednu '%A' - puni naziv, a '%a' - skraceni naziv")
print(f"Puni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%A')}.")
print(f"Skraćeni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%a')}.")


locale.setlocale(locale.LC_TIME, 'hr_HR')
print(f"HRV Puni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%A')}.")
print(f"HRV Skraćeni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%a')}.")
print(f"HRV Puni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%A')[:3]}.")

locale.setlocale(locale.LC_ALL, '')

# Ispis godine
print("\nTekuca godina '%Y' - puni naziv, a '%y' - skraceni naziv")
print(f"4 znamenke - Tekuca godine je {danasnji_dan.strftime('%Y')}. godina")
print(f"2 znamenke - Tekuca godine je {danasnji_dan.strftime('%y')}. godina")

print("\nBroj danasnjeg dana u godini: '%j'")
print(f"Danas je {danasnji_dan.strftime('%j')}. dan u {danasnji_dan.strftime('%Y')}. godini")

print("\nBroj tjedna u godini: '%W'")
print(f"Danas je {danasnji_dan.strftime('%W')}. tjedan u {danasnji_dan.strftime('%Y')}. godini")


# Ispis mjeseca
print("\nTekuci mjesec '%B' - puni naziv, a '%b' - kraci naziv, a '%m' - broj")
print(f"Puni naziv mjeseca je {danasnji_dan.strftime('%B')}")
print(f"KRaci naziv mjeseca je {danasnji_dan.strftime('%b')}")
print(f"Danasnji mjeseca je {danasnji_dan.strftime('%m')}")

# Kombinirani prikaz
print("\n\Komniniranje prikaza pomocu strftime()\n")
print(f"Sadasnji trenutak: {sadasnji_trenutak.strftime('%A')}, {sadasnji_trenutak.strftime('%d.%m.%Y. %H:%M:%S')}")