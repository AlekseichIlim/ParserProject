from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db_manager import get_themes_list, get_rating_list, get_problems_with_theme_and_rating
from src.models import Problem, Base


def test_get_themes_list(db_session):
    """Тестирует получение тем задач"""

    themes = db_session.query(Problem.tags).all()

    assert themes is not None
    assert 'math' in get_themes_list(db_session)
    assert type(get_themes_list(db_session)) == list


def test_get_rating_list(db_session):
    """Тестирует получение сложности задач"""

    ratings = db_session.query(Problem.rating).distinct()

    assert ratings is not None
    assert type(get_rating_list(db_session)) == list


def test_get_problems_with_theme_and_rating_1(db_session, user_text_1, user_text_2):
    """Тестирует получение списка всех задач, по указанной теме и сложности"""

    result = get_problems_with_theme_and_rating(db_session, user_text_1, user_text_2)

    assert result is not None
    assert type(result) == list


def test_get_problems_with_theme_and_rating_2(db_session, user_text_1, user_text_3):
    """Тестирует получение списка всех задач, по указанной теме и сложности"""

    result = get_problems_with_theme_and_rating(db_session, user_text_1, user_text_3)

    assert result is None
