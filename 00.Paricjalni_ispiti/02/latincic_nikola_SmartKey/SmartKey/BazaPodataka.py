import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Family(Base):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    pin = db.Column(db.String)
    active = db.Column(db.Boolean)


# ---- FUNKCIJE ----
def add_person(session, first_name, last_name, pin, active=bool):
    """Dodaj novu osobu u bazu podataka, ako osoba već ne postoji"""
    person = (
        session.query(Family)
        .filter(db.and_(Family.first_name == first_name, Family.last_name == last_name))
        .filter(Family.pin == pin)
        .one_or_none()
    )
    if person is None:
        person = Family(
            first_name=first_name, last_name=last_name, pin=pin, active=active
        )
    session.add(person)
    session.commit()


def get_all_family_members(session):
    """ohvaća sve članove obitelji iz Baze podataka"""
    return session.query(Family).order_by(Family.id).all()


def get_user_by_pin(session, pin):
    """Dohvaća člana obitelji iz Baze podataka po pin broju"""
    user = session.query(Family).filter(Family.pin == pin)
    if user:
        return True
    else:
        return False


def get_user(session, first_name, last_name, pin):
    """Dohvaća jednog člana obitelji iz Baze podataka"""
    user = (
        session.query(Family)
        .filter(db.and_(Family.first_name == first_name, Family.last_name == last_name))
        .filter(Family.pin == pin)
    )
    if user and user.active:
        return True
    else:
        return False


def edit_user(session, id, new_first_name, new_last_name, new_pin, new_activity):
    """Pronalazi člana obitelji iz Baze podataka prema id broju i uređuje podatke za njega"""
    user = session.query(Family).filter(Family.id == id)
    if user:
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.pin = new_pin
        user.active = new_activity
        session.commit()
        return True
    else:
        return False


def delete_user(session, id):
    """Pronalazi člana obitelji iz Baze podataka prema id broju i briše ga iz baze"""
    user = session.query(Family).filter(Family.id == id)
    if user:
        session.delete(user)
        session.commit()
        return True
    else:
        return False


def create_engine(path):
    db_engine = db.create_engine(f"sqlite:///{path}")
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()
    return session
