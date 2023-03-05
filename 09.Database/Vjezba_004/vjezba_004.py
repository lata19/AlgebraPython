import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

# za spajanje na bazu koristimo "engine"
# da nije lokalna datoteka: "sqlite://"
CONN_STR = "sqlite:///9.Database/Vjezba_002_CRUD/CompanyDB.db"
db_engine = db.create_engine(CONN_STR)
db_connection = db_engine.connect()
db_metadata = db.MetaData()
employees = db.Table("Employees", db_metadata, autoload_with=db_engine)

# print(employees.columns)
# zamjena za SELECT * FROM Employees ...
sql_select_upit = db.select(employees)

# Kreirajmo jedan objekt koji cemo koristiti kao proxy (posrednika) za pristup podacima
ResultProxy = db_connection.execute(sql_select_upit)

# ResultSet je naziv za listu redaka procitanih iza baze. Jednostavnije, to je tabela.
# Iskoristimo ResultProxy objekt da dohvatimo sve fetchall() i kreiramo novu "tabelu"
ResultSet = ResultProxy.fetchall()

# U slucaju da imamo jako puno podataka mozemo dohvatiti samo njih 20.
# Umjesto fetchall() koristimo .fetchmany(20) i damo broj koliko redaka zelimo
PartialResultSet = ResultProxy.fetchmany(20)

# Procitajmo jedan po jedan objekt
for result in ResultSet:
    print(result)