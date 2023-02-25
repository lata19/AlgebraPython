import sqlite3

database_name = "9.Database/Vjezba_002/CompanyDB.db"

select_query = "SELECT * FROM Employees WHERE id=?"

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print("Baza je uspješno kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(select_query, (3,))
    records = cursor.fetchall()

    for record in records:
        print(record)

    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspješno otpušteni.")
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatovrena.")