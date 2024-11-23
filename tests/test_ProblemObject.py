from src.ProblemObject import ProblemObject


def test_init(problems_fix_1):
    """
    Тестирует __init__
    """
    assert problems_fix_1.contest_id == 'A'
    assert problems_fix_1.index == '123'
    assert problems_fix_1.name == 'Задача-задача'
    assert problems_fix_1.tags == 'math'
    assert problems_fix_1.rating == 500
    assert problems_fix_1.solved_count == 1000


def test_str(capsys):
    """
    Тестирует print экземпляра
    """
    test_p = ProblemObject('A', 123, 'Задача-задача', 'math', 1000, 500)
    print(test_p)
    message = capsys.readouterr()
    assert message.out == ('Задача № A_123. Задача-задача. Темы: math. Сложность: 1000. Количество решений: 500\n')


def test_get_to_object_list_1(consolidation_lists_fix):
    """
    Тестирует метод создания списка объектов класса ProblemObject
    """
    p = ProblemObject.get_to_object_list(consolidation_lists_fix)
    assert type(p) == list


def test_cast_to_object_2(objects_fix_1):
    """
    Проверяет класс объектов в списке
    """
    for i in objects_fix_1:
        assert type(i) == ProblemObject


def test_get_to_compilation_1(data_fix):
    """
    Тестирует метод создания списка объектов класса ProblemObject
    """

    p = ProblemObject.get_to_compilation(data_fix)
    assert type(p) == list