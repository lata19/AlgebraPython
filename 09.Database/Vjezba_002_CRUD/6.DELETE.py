import sqlite3

database_name = "9.Database/Vjezba_002/CompanyDB.db"

delete_records_query = "DELETE FROM Employees WHERE id = ?"

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print("Baza je uspješno kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(delete_records_query, (3,))
    sqliteConnection.commit()
    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspješno otpušteni.")
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatovrena.")