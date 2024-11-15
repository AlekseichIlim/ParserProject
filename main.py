from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config
from src.db_manager import DBManager
from src.Codeforces_API import ProblemCodeforcesAPI
from src.utils import DATABASE_URL, create_table, save_data_problems, create_problems_objects

params = config()

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

problems = ProblemCodeforcesAPI()
problems.load_data()

#создает списки зачач и статистики из API
problems_list = problems.get_problems()
problems_statistics = problems.get_problems_statistics()


#создаем таблицу в БД и сохраняем данные из API в таблицу
create_table(engine)
save_data_problems(problems_list, problems_statistics, session)


# #создаем экземпляр менеджера БД
# data_bd = DBManager()
#
# # делаем выборку данных с БД
# problems_sort = data_bd.get_problems_with_theme(session, 'math', 1000)
#
# problems_objects = create_problems_objects(problems_sort)
#
# for problem in problems_objects:
#     print(problem)
#
# print(len(problems_statistics))