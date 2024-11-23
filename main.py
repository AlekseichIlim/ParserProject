from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_manager import create_table, save_data_problems
from src.functions import main
from src.utils import DATABASE_URL


engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    main(engine, session)
