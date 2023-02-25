import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "Employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

# za spajanje na bazu koristimo "engine"

db_engine = db.create_engine("sqlite:///9.Database/Vjezba_002_CRUD/CompanyDB.db")
db_connection = db_engine.connect()
db_metadata = db.MetaData()
employees = db.Table("Employees", db_metadata, autoreload=True, autoload_with=db_engine)

sql_select_query = db.select([])