from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, Boolean
from sqlalchemy.orm import sessionmaker
from datetime import timedelta


class Database:
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

    def __str__(self):
        return "Task:{} | Start: {} |End: {}".format(
            self.description,
            self.date_start,
            self.date_stop
        )

    def get_duration(self):
        duration = str(self.date_stop - self.date_start)
        return duration


class PomodoroTask(Base):
    __tablename__ = "pomodoro"
    id = Column(Integer, primary_key=True)
    date = Column(DATETIME)

    def __str__(self):
        return "Date:{}".format(
            self.date
        )

class PomodoroSettings(Base):
    __tablename__ = "pomodoroSettings"
    id = Column(Integer, primary_key=True)
    pomodoro_length = Column(Integer)
    pause_length = Column(Integer)
    has_auto_pause = Column(Boolean)
    has_auto_pomodoro = Column(Boolean)
       

Base.metadata.create_all(db.engine)
