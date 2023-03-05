import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

# many-to-many relacija autor-izdavac
# svaki autor moze imati vise izdavaca i obratno
autor_izdavac = db.Table(
    "autor_izdavac", 
    Base.metadata, 
    db.Column("autor_id", db.Integer, db.ForeignKey("autor.id")), 
    db.Column("izdavac_id", db.ForeignKey("izdavac.id"))
)

knjiga_izdavac = db.Table(
    "knjiga_izdavac",
    Base.metadata,
    db.Column("knjiga_ide", db.Integer, db.ForeignKey("knjiga.id")),
    db.Column("izdavac_id", db.ForeignKey("izdavac.id"))
)


"""
    CREATE TABLE autor (
        id INTEGER PRIMARY KEY,
        ime VARCHAR,
        prezime VARCHAR 
    )
"""

class Autor(Base):
    # ime tablice definiramo na ovaj način
    __tablename__ = "autor"
    # popis stupaca
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)
    # Svaki autor ima kolekciju knjiga
    # Klasa knjiga imati će povratnu referencu na tabelu autor
    # 1-to-many relationship
    knjige = relationship("Knjiga", backref=backref("autor"))
    # many-to-many relacija
    # prethodno moramo kreirati tablicu
    izdavaci = relationship("Izdavac", secondary=autor_izdavac, back_populates="autori")

"""
    CREATE TABLE knjiga (
        id INTEGER PRIMARY KEY,
        autor_id INTEGER REFERENCES autor,
        naslov VARCHAR
    )
"""

class Knjiga(Base):
    __tablename__ = "knjiga"
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"))
    naslov = db.Column(db.String)
    izdavaci = relationship("Izdavac", secondary=knjiga_izdavac, back_populates="knjige")

"""
    CREATE TABLE izdavac (
        id INTEGER PRIMARY KEY,
        naziv VARCHAR
    )
"""

class Izdavac(Base):
    __tablename__ = "izdavac"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)
    autori = relationship("Autor", secondary=autor_izdavac, back_populates="izdavaci")
    knjige = relationship("Knjiga", secondary=knjiga_izdavac, back_populates="izdavaci")

