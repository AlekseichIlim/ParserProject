from src.functions import get_compilation_problems


def test_get_compilation_problems_1(db_session, user_text_1, user_text_2):
    """Тестирует получение подборки задач"""

    result = get_compilation_problems(db_session, user_text_1, user_text_2)

    assert result is not None
    assert type(result) == list
    assert len(result) == 10

def test_get_compilation_problems_2(db_session, user_text_1, user_text_3):
    """Тестирует получение подборки задач"""

    result = get_compilation_problems(db_session, user_text_1, user_text_3)

    assert result is not None
    assert type(result) == list
    assert len(result) == 0