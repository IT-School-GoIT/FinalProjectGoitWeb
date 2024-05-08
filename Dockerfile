# Використовуємо офіційний образ Python
FROM python:3.8

# Встановлюємо PostgreSQL та інші необхідні пакети
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

WORKDIR /app

# Встановлюємо інструмент 'wait-for-it'
RUN apt-get update && apt-get install -y wait-for-it

# Встановлюємо залежності
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копіюємо всі файли проекту в контейнер
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Команда запуску сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
