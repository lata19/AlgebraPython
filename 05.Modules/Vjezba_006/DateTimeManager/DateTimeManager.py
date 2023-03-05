import datetime as dt
import dateutil as tz

def dateConverter(date):
    """
    Funkcija koja za upisan datum i vrijeme pretvara upis u format datuma u formatu: DD.MM.YYYY. HH:MM
    """
    return dt.datetime.strptime(date, "%d. %B %Y. %H:%M")

def timeBeforeAppointment(oib, appointment):
    """
    Funkcija koja računa koliko je još vremena ostalo da sljedećeg termina.
    """
    pass
