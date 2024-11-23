from src.db_manager import get_problems_with_theme_and_rating


class ProblemObject:
    def __init__(self,  contest_id, index, name, tags, rating, solved_count):

        self.index = index
        self.name = name
        self.tags = tags
        self.solved_count = solved_count
        self.contest_id = contest_id
        self.rating = rating

    def __str__(self):
        return f'Задача № {self.contest_id}_{self.index}. {self.name}. Темы: {self.tags}. Сложность: {self.rating}. Количество решений: {self.solved_count}'

    @classmethod
    def get_to_object_list(cls, list_problems):
        """
        Преобразование набора данных из списка задач в список объектов класса ProblemObject
        """
        object_list = []
        for problem in list_problems:
            if problem.get('rating'):
                object_list.append(
                    cls(problem['contestId'], problem['index'], problem['name'], problem['tags'], problem['rating'],
                        problem['solvedCount']))
            else:
                object_list.append(
                    cls(problem['contestId'], problem['index'], problem['name'], problem['tags'], None,
                        problem['solvedCount']))
        return object_list

    @classmethod
    def get_to_compilation(cls, problems_filter_list):
        """
        Возвращает подборку объектов отсортированных задач
        """

        object_list = []
        for problem in problems_filter_list:
            object_list.append(
                cls(problem.contest_id, problem.index, problem.name, problem.tags, problem.rating,
                    problem.solved_count))

        return object_list

