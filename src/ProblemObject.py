class ProblemObject:
    def __init__(self, contest_id, index, name, tags, rating, solved_count):
        self.contest_id = contest_id
        self.index = index
        self.name = name
        self.tags = tags
        self.rating = rating
        self.solved_count = solved_count

    def __str__(self):
        return f'Задача № {self.contest_id}_{self.index}. {self.name}. Темы: {self.tags}. Сложность: {self.rating}. Количество решений: {self.solved_count}'