import requests


class ProblemCodeforcesAPI:
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

        response = requests.get(self.__url, params={'lang': 'ru'})
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
