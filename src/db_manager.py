from src.models import Problem, Base
from sqlalchemy.exc import IntegrityError


def create_table(engine):
    """Создание всех таблиц в базе данных"""

    Base.metadata.create_all(engine)


def save_data_problems(objects, session):
    """Заполнение базы данных"""

    for problem in objects:
        try:
            new_problem = Problem(
                contest_id=problem.contest_id,
                index=problem.index,
                name=problem.name,
                tags=(', '.join(problem.tags)),
                rating=problem.rating,
                solved_count=problem.solved_count
            )
            session.add(new_problem)
            session.commit()
        except IntegrityError:
            session.rollback()
            continue

    session.close()


def get_themes_list(session):
    """Получает список всех тем задач"""

    themes = session.query(Problem.tags).all()
    themes_list = []

    for item in themes:
        theme = ', '.join(item)
        themes_list.extend(theme.split(', '))

    session.close()

    return set(themes_list)


def get_rating_list(session):
    """Получает список сложности задач"""

    ratings = session.query(Problem.rating).all()
    rating_list = []

    for i in ratings:
        rating_list.append(i)

    session.close()

    return set(rating_list)


def get_problems_with_theme_and_rating(session, theme, rating):
    """Получает список всех задач, по указанной теме и сложности"""

    problems_filter = session.query(Problem).filter(Problem.tags.ilike(f'%{theme}%'), Problem.rating == rating).all()

    session.close()

    return problems_filter
