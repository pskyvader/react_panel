from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os
import json

from sqlalchemy import Column


config=[]
if len(config) == 0:
    config_path=os.path.join(os.path.dirname(__file__), "..",'config','config.json')
    with open(config_path) as f:
        config = json.load(f)

# connection_string="mysql+mysqlconnector://{}:{}@{}/{}".format(config["user"],config["password"],config["host"],config["database"])
connection_string="mysql://{}:{}@{}/{}".format(config["user"],config["password"],config["host"],config["database"])
# connection_string='sqlite:///database.sqlite3'

engine = create_engine(connection_string, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from .models import logo_model,administrador_model

    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    add_if_not_exists(logo_model,titulo='favicon',orden=1)
    add_if_not_exists(logo_model,titulo='Logo login',orden=2)
    add_if_not_exists(logo_model,titulo='Logo panel grande',orden=3)
    add_if_not_exists(logo_model,titulo='Logo panel pequeño',orden=4)
    add_if_not_exists(logo_model,titulo='Logo Header sitio',orden=5)
    add_if_not_exists(logo_model,titulo='Logo Footer sitio',orden=6)
    add_if_not_exists(logo_model,titulo='Manifest',orden=7)
    add_if_not_exists(logo_model,titulo='Email',orden=8)
    add_if_not_exists(administrador_model,tipo=1,email='admin@mysitio.cl',password=encript('12345678'),nombre='Admin',estado=True)

    db_session.commit()


def add_if_not_exists(model,**kwargs):
    instance = db_session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        db_session.add(instance)


def encript(password):
    import hashlib

    part1 = hashlib.sha256()
    part1.update(password.encode("utf-8"))
    part2 = hashlib.sha256()
    part2.update(part1.hexdigest().encode("utf-8"))
    password = part1.hexdigest() + part2.hexdigest()
    return password