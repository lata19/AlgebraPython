import sqlite3

create_table_query = """CREATE TABLE IF NOT EXISTS Employees (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE);"""
database_name = "9.Database/Vjezba_002/CompanyDB.db"

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print("Baza je uspješno kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(create_table_query)
    sqliteConnection.commit()
    print("Nova tablica Employees je uspješno kreirana")
    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspješno otpušteni.")
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatovrena.")