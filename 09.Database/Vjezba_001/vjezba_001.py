import sqlite3

select_query = "Select sqlite_version();"

try:
    sqliteConnection = sqlite3.connect("9.Database/Vjezba_001/SQLite_Python.db")
    cursor = sqliteConnection.cursor()
    print("Baza je uspješno kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(select_query)
    records = cursor.fetchall()
    print("SQLite verzija je:", records)

    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspješno otpušteni.")

except sqlite3.Error as error:
    print("Dogodila se greška prilikom pokušaja spajanja na SQLite:", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspješno zatvorena.")