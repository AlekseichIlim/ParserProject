from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Table, UniqueConstraint

Base = declarative_base()


class Problem(Base):
    __tablename__ = 'problem'

    contest_id = Column(Integer, primary_key=True, nullable=True)
    index = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    tags = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)
    solved_count = Column(Integer, nullable=True)
    UniqueConstraint('contest_id', 'index', name='uniq_id')
