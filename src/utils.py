import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from src.ProblemObject import ProblemObject
from src.models import Base, Problem

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


def create_table(engine):
    """Создание всех таблиц в базе данных"""

    Base.metadata.create_all(engine)


def save_data_problems(problems, problems_statistics, session):
    """Заполнение базы данных"""

    for problem in problems:
        for item in problems_statistics:
            try:
                new_problem = Problem(
                    contest_id=problem['contestId'],
                    index=problem['index'],
                    name=problem['name'],
                    tags=(', '.join(problem['tags'])),
                    rating=problem['rating'],
                    solved_count=item['solvedCount']
                )
                session.add(new_problem)
                session.commit()
            except IntegrityError:
                session.rollback()
                continue

    session.close()


def create_problems_objects(data):
    """Создание списка объектов ProblemObjects из полученных данных"""

    problems = []

    for item in data:
        problem = ProblemObject(item.contest_id,
                                item.index,
                                item.name,
                                item.tags,
                                item.rating,
                                item.solved_count
                                )
        problems.append(problem)

    return problems
