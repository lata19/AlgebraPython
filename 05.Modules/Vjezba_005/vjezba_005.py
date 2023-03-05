import datetime as dt
from dateutil import tz


# meeting_time = input("Upišite datum i vrijeme sastanka u formatu: dan. naziv_mjeseca godina. sati:minuta - ")
meeting_time = "20. February 2023. 14:00"
meeting_time_format = dt.datetime.strptime(meeting_time, "%d. %B %Y. %H:%M")

current_time = dt.datetime.now()

time_before_start = meeting_time_format - current_time

print(f"Vaš sastanak počinje za {time_before_start}")



