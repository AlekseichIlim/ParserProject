import random

from src.Codeforces_API import ProblemCodeforcesAPI
from src.ProblemObject import ProblemObject
from src.db_manager import create_table, save_data_problems, get_problems_with_theme_and_rating


def get_compilation_problems(session, theme, rating):
    """Возвращает подборку из 10 задач по заданной теме и сложности"""

    list_problems_sort = get_problems_with_theme_and_rating(session, theme, rating)

    if list_problems_sort is not None:
        problems = ProblemObject.get_to_compilation(list_problems_sort)

        random.shuffle(problems)

        return problems[:10]
    else:
        return []


def main(engine, session):

    # создает экземпляр API Codeforces для получения списков задач
    problems = ProblemCodeforcesAPI()

    # создает список данных о задачах
    problems_list = problems.get_consolidation_lists()

    # создает список объектов класса ProblemObject
    object_list = ProblemObject.get_to_object_list(problems_list)

    # создает таблицу в БД
    create_table(engine)

    # сохраняем данные из API в таблицу БД
    save_data_problems(object_list, session)
