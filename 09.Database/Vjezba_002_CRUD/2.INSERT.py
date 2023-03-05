import sqlite3

database_name = "9.Database/Vjezba_002/CompanyDB.db"

insert_into_table_query = """   INSERT INTO Employees (name, email)
                                VALUES (?, ?)"""

lista_djelatnika = [
    ('Petar Peric', 'pperic@gmail.com'),
    ('Ana Anic', 'aanic@gmail.com'),
    ('Kresimir Horvat', 'khorvat@gmail.com')
]

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()

    for djelatnik in lista_djelatnika:
        cursor.execute(insert_into_table_query, djelatnik)

    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatovrena.")