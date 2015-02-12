#! /usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime



class Person(Base):
      __tablename__ = "person"
      id = Column(Integer, primary_key=True)
      name = Column(String, nullable=False)     
      passport = relationship("Passport", uselist=False, backref="owner")
      
class Passport(Base):
      __tablename__ = 'passport'
      id = Column(Integer, primary_key=True)
      issue_date = Column(Date, nullable=False, default=datetime.utcnow)
      owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)    

Base.metadata.create_all(engine)

krishna = Person(name="krish")
session.add(krishna)

passport = Passport()
krishna.passport = passport
session.add(passport)
session.commit()


print krishna.passport.issue_date
print passport.owner.name
