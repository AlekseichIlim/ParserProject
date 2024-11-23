import schedule

from src.functions import main

schedule.every().hour.do(main)

while True:
    schedule.run_pending()
