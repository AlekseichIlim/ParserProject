class ProblemObject:
    def __init__(self,  index, name, tags, solved_count, contest_id, rating):

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
                    cls(problem['index'], problem['name'], problem['tags'], problem['solvedCount'],
                        problem['contestId'], problem['rating']))
            else:
                object_list.append(
                    cls(problem['index'], problem['name'], problem['tags'], problem['solvedCount'],
                        problem['contestId'], None))
        return object_list
