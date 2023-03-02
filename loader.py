import os
import dotenv
dotenv.load_dotenv()
from sqlalchemy import (Column,func,
String as varchar,MetaData,ForeignKey,create_engine,Integer,DateTime,Table,and_,or_,not_)
from sqlalchemy.orm import declarative_base,sessionmaker,Session


url = os.environ.get('URL')

engine = create_engine(url)

con = engine.connect()

Base = declarative_base()

SSession = sessionmaker(engine)

session = SSession()