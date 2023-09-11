from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def save(self):
        Session = sessionmaker()
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @classmethod
    def create_table(cls):
        engine = create_engine('sqlite:///dogs.db')
        Base.metadata.create_all(engine)

    @classmethod
    def new_from_db(cls, row):
        return cls(**dict(row))

    @classmethod
    def get_all(cls):
        return [cls.new_from_db(row) for row in cls.query.all()]

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)
