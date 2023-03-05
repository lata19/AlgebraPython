import datetime as dt


start = input("Upišite datum početka sezone: u formatu (dan. naziv_mjeseca godina. sati:minuta) - ")
end = input("Upišite datum završetka sezone: u formatu (dan. naziv_mjeseca godina. sati:minuta) - ")
season_start = dt.datetime.strptime(start, "%d. %B %Y. %H:%M")
season_end = dt.datetime.strptime(end, "%d. %B %Y. %H:%M")

# Provjera koji je dan u tjednu početak sezone
if dt.date.weekday(season_start) == 0:
    date = season_start + dt.timedelta(days=2)
elif dt.date.weekday(season_start) == 1:
    date = season_start + dt.timedelta(days=1)
elif dt.date.weekday(season_start) == 2:
    date = season_start
elif dt.date.weekday(season_start) == 3:
    date = season_start + dt.timedelta(days=3)
elif dt.date.weekday(season_start) == 4:
    date = season_start + dt.timedelta(days=2)
elif dt.date.weekday(season_start) == 5:
    date = season_start + dt.timedelta(days=1)
elif dt.date.weekday(season_start) == 6:
    date = season_start


i = 1
print(f"Raspored utakmica za sezonu {season_start.strftime('%Y')}./{season_end.strftime('%Y')}.")

while date <= season_end:
    if dt.date.weekday(date) == 2:
        print(f"{i}. {date.strftime('%A')}, {date.strftime('%d.%m.%Y %H:%M')}")
        # print("{:<2} {:<12} {:<25}".format(i, date.strftime('%A'), date))
        date += dt.timedelta(days=4)
        i += 1
        if date <= season_end:
            print(f"{i}. {date.strftime('%A')}, {date.strftime('%d.%m.%Y %H:%M')}")
            # print("{:<2} {:<12} {:<25}".format(i, date.strftime('%A'), date))
        date += dt.timedelta(days=10)
    
    elif dt.date.weekday(date) == 6:
        print(f"{i}. {date.strftime('%A')}, {date.strftime('%d.%m.%Y %H:%M')}")
        # print("{:<2}. {:<12} {:<25}".format(i, date.strftime('%A'), date))
        date += dt.timedelta(days=3)
        i += 1
        if date <= season_end:
            print(f"{i}. {date.strftime('%A')}, {date.strftime('%d.%m.%Y %H:%M')}")
            # print("{:<2} {:<12} {:<25}".format(i, date.strftime('%A'), date))
        date += dt.timedelta(days=11)
    
    i += 1