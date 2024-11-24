FROM python:3-slim


WORKDIR /app

# Копируем только файл с зависимостями
COPY /requirements.txt /

# Устанавливаем pip и зависимости
RUN pip install -r /requirements.txt --no-cache-dir

COPY . .

CMD ["sh", "-c", "python main.py && python start_bot.py && python /src/startscheduler.py"]