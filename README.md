Приложение парсит данные о задачах с сервиса Codeforces, сохраняет их в БД, а также обновляет данные каждый час. Телеграмм бот позволяет искать и получать задачи по теме и сложности, выводит подборку из 10 задач.

Запуск без DOCKER:
1. Переименовать файл '.env.sample' в '.env', в нем вставить свои данные в переменные DATABASE_URL и TELEGRAM_TOKEN.
2. Установить зависимости 'pip install -r requirements.txt'.
3. Запустить приложение 'python main.py && python start_bot.py && python /src/startscheduler.py'
