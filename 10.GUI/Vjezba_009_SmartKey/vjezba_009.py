import os
import tkinter as tk
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

# root = tk.Tk()
# root.title("Smart Key")

Base = declarative_base()


class Family(Base):
    __tablename__ = "Family"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    role = db.Column(db.String)


# ---- FUNKCIJE (CRUD) ----
def get_persons(session):
    return session.query(Family).order_by(Family.age).all()


def add_person(
    session,
    first_name,
    last_name,
    gender,
    age,
    role,
):
    """Dodaj novu osobu u bazu podataka, ako osoba već ne postoji"""
    person = (
        session.query(Family)
        .filter(db.and_(Family.first_name == first_name, Family.last_name == last_name))
        .filter(Family.role == role)
        .one_or_none()
    )
    if person is None:
        person = Family(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            age=age,
            role=role,
        )
    session.add(person)
    session.commit()


def main():
    db_engine = db.create_engine("sqlite:///10.GUI/Vjezba_009_SmartKey/Family.db")
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    family = []

    for person in family:
        add_person(
            session,
            first_name=person[0],
            last_name=person[1],
            gender=person[2],
            age=person[3],
            role=person[4],
        )

    persons = get_persons(session)
    for person in persons:
        print(f"Ime: {person.first_name}")
        print(f"Prezime: {person.last_name}")
        print(f"Spol: {person.gender}")
        print(f"Godine: {person.age}")
        print(f"Uloga u obitelji: {person.role}")


main()

# root.mainloop()
