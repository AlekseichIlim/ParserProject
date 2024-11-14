import pytest
from src.ProblemObject import ProblemObject


def test_init(problems_fix_1):
    """
    Тестирует __init__
    """
    assert problems_fix_1.contest_id == 123
    assert problems_fix_1.index == 'A'
    assert problems_fix_1.name == 'Задача-задача'
    assert problems_fix_1.tags == 'math'
    assert problems_fix_1.rating == 1000
    assert problems_fix_1.solved_count == 500


def test_str(capsys):
    """
    Тестирует print экземпляра
    """
    test_p = ProblemObject(123, 'A', 'Задача-задача', 'math', 1000, 500)
    print(test_p)
    message = capsys.readouterr()
    assert message.out == ('Задача № 123_A. Задача-задача. Темы: math. Сложность: 1000. Количество решений: 500\n')


# def test_cast_to_object_2(problems_fix_1):
#     """
#     Проверяет класс объектов в списке
#     """
#     for i in problems_fix_1:
#         assert type(i) == ProblemObject


