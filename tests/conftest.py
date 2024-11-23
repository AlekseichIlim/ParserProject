import pytest
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from src.ProblemObject import ProblemObject
from src.db_manager import create_table, save_data_problems
from src.models import Problem


class ProblemCodeforcesAPI:
    """
    Класс для работы с API Codeforces
    """

    def __init__(self):
        self.__url = 'https://codeforces.com/api/problemset.problems'
        self.problems = []
        self.problems_statistics = []
        self.params = {'tags': 'math'}

    def load_data(self):
        """
        Создает списки, задач и статистики
        """

        response = requests.get(self.__url, params=self.params)
        problems = response.json()['result']['problems']
        problems_stat = response.json()['result']['problemStatistics']
        self.problems.extend(problems)
        self.problems_statistics.extend(problems_stat)

    def get_problems(self):
        """
        Возвращает список задач
        """
        self.load_data()

        return self.problems

    def get_problems_statistics(self):
        """
        Возвращает список статистики по задачам
        """
        self.load_data()

        return self.problems_statistics

    def get_consolidation_lists(self):
        """
        Объединяет списки задач и статистики
        """

        self.load_data()

        for problem, stat in zip(self.problems, self.problems_statistics):
            problem['solvedCount'] = stat['solvedCount']

        return self.problems


@pytest.fixture
def db_session(objects_fix_1):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    create_table(engine)

    save_data_problems(objects_fix_1, session)

    return session


@pytest.fixture
def data_fix(db_session):
    problems_filter = db_session.query(Problem).filter(Problem.tags.ilike('%math%'),
                                                       Problem.rating == 1000).all()

    return problems_filter


@pytest.fixture
def problems_fix():
    tests_API = ProblemCodeforcesAPI()
    return tests_API.get_problems()


@pytest.fixture
def problems_stat_fix():
    tests_API = ProblemCodeforcesAPI()
    return tests_API.get_problems_statistics()


@pytest.fixture()
def consolidation_lists_fix():
    tests_API = ProblemCodeforcesAPI()
    return tests_API.get_consolidation_lists()


@pytest.fixture
def problems_fix_1():
    return ProblemObject('A', '123', 'Задача-задача', 'math', 500, 1000)


@pytest.fixture
def objects_fix_1(consolidation_lists_fix):
    objects_list = ProblemObject.get_to_object_list(consolidation_lists_fix)
    return objects_list


# @pytest.fixture
# def objects_api_1():
#     obj_list = [
#         {'contestId': 'A', 'index': 123, 'name': 'problem', 'tags': 'math', 'solvedCount': 100,
#          , 'rating': 400},
#         {'index': 123, 'name': 'problems', 'tags': 'math', 'solvedCount': 100,
#          'contestId': 'A', 'rating': 400},
#         {'index': 123, 'name': 'problem', 'tags': 'math', 'solvedCount': 100,
#          'contestId': 'A'},
#         {'index': 123, 'name': 'problems', 'tags': 'math', 'solvedCount': 100,
#          'contestId': 'A', 'rating': 400},
#     ]
#     return obj_list


# @pytest.fixture
# def objects_api_2():
#     obj = {'index': 123, 'name': 'problem', 'tags': 'math', 'solvedCount': 100,
#            'contestId': 'A'}
#     return obj


@pytest.fixture
def user_text_1():
    return 'math'


@pytest.fixture
def user_text_2():
    return 800


@pytest.fixture
def user_text_3():
    return 7000