import sqlite3

database_name = "9.Database/Vjezba_002/CompanyDB.db"

update_table_query = """UPDATE Employees
                        SET name = ?,
                            email = ?
                        WHERE id = ?"""

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print("Baza je uspješno kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(update_table_query, ('Ana Anica Horvat', 'aahorvat@gmail.com', 2))
    sqliteConnection.commit()
    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspješno otpušteni.")
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatovrena.")