from src.models import Problem


class DBManager:
    """
    Класс для работы с данными в БД
    """

    def get_problems_with_theme(self, session, theme, rating):
        """Получает список всех задач, по указанной теме и сложности"""

        problems = session.query(Problem).filter(Problem.tags.ilike(f'%{theme}%'), Problem.rating == rating).all()

        return problems
