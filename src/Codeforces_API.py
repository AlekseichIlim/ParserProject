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

    def __init__(self, theme):
        self.__url = 'https://codeforces.com/api/problemset.problems'
        # self.__method = {'problemset.problems'}
        self.__params = {'tags': ''}
        self.problems = []
        self.problems_statistics = []
        self.theme = theme

    def load_data(self):
        """
        Создает списки, задач по теме и статистики по задачам
        """

        theme = self.theme
        self.__params['tags'] = theme.lower()
        response = requests.get(self.__url, params=self.__params)
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

        return self.problems


a = ProblemCodeforcesAPI('brute force')
print(a.get_problems)