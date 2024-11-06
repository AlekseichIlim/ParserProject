from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, List, ForeignKey

Base = declarative_base()


class Problem(Base):
    __tablename__ = 'problem'

    contest_id = Column(Integer, primary_key=True, nullable=True)
    index = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    tags = Column(List, nullable=False)

    rating = Column(Integer, nullable=True)


class ProblemStatistics(Base):
    __tablename__ = 'problem_statics'

    contest_id = Column(Integer, ForeignKey('problem.contest_id'))
    problem_index = Column(String, ForeignKey('problem.index'))
    solved_count = Column(Integer, nullable=False)

    Column(Integer, ForeignKey('authors.id'))