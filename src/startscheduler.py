import schedule


def task():
    print("I'm working...")

schedule.every().second.do(task)

while True:
    schedule.run_pending()
