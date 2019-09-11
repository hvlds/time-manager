from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import sessionmaker


class Database():
    def __init__(self):
        db_uri = "sqlite:///db.sqlite"
        self.engine = create_engine(db_uri)
        self.connection = self.engine.connect()
        Session = sessionmaker(self.engine)
        self.session = Session()


db = Database()
Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    date_start = Column(DATETIME)
    date_stop = Column(DATETIME)

Base.metadata.create_all(db.engine)
