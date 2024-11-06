import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.models import Base

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)

# Добавление нового пользователя в базу данных
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()
session.close()