from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

## Setup database + engine
DATABASE_URL = "mysql://root:rootpassword@single_compose-mysqldb-1:3306/pollutions"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()