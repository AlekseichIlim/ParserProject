import requests
from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __init__(self):
        self.__url = ''
        self.__params = {}

    @abstractmethod
    def load_data(self):
        pass


class ProblemCodeforcesAPI(Parser):
    """
    Класс для работы с API Codeforces
    """

    def __init__(self):
        self.__url = 'https://codeforces.com/api/problemset.problems'
        self.problems = []
        self.problems_statistics = []

    def load_data(self):
        """
        Создает списки, задач и статистики
        """

        response = requests.get(self.__url)
        problems = response.json()['result']['problems']
        problems_stat = response.json()['result']['problemStatistics']
        self.problems.extend(problems)
        self.problems_statistics.extend(problems_stat)

    def get_problems(self):
        """
        Возвращает список задач
        """

        return self.problems

    def get_problems_statistics(self):
        """
        Возвращает список статистики по задачам
        """

        return self.problems_statistics


# a = ProblemCodeforcesAPI()
# a.load_data()
# # b = a.get_problems
# # print(b.count())
# b = a.problems
# print(len(b))
# print(b)
# print(b.count())
# print(a.problems)