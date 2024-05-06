# Використовуємо офіційний образ Python
FROM python:3.8

# Встановлюємо PostgreSQL та інші необхідні пакети
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

WORKDIR /app

# Встановлюємо інструмент 'wait-for-it'
RUN apt-get update && apt-get install -y wait-for-it

# Встановлюємо залежності
COPY requirements.txt /app/requirements.txt
COPY manage.py /app/manage.py
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копіюємо всі файли проекту в контейнер
COPY . /app


# Встановлюємо робочу директорію
WORKDIR /app

# Команда запуску сервера Django
CMD ["sh", "-c", "wait-for-it postgres:5432 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]





# #_______________Для запуску без compose___________________________________________

# # Використовуємо офіційний образ Python
# FROM python:3.8

# # Встановлюємо PostgreSQL та інші необхідні пакети
# RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# WORKDIR /app

# # Встановлюємо інструмент 'wait-for-it'
# RUN apt-get update && apt-get install -y wait-for-it

# # Встановлюємо залежності
# COPY requirements.txt /app/requirements.txt
# COPY manage.py /app/manage.py
# RUN pip install --no-cache-dir -r /app/requirements.txt

# # Копіюємо всі файли проекту в контейнер
# COPY . /app

# # Налаштовуємо змінні середовища для підключення до PostgreSQL
# ENV DB_NAME=neondb
# ENV DB_USER=neondb_owner
# ENV DB_PASSWORD=ZbeF0sXW2IHK
# ENV DB_HOST=ep-winter-boat-a5gpzr8g.us-east-2.aws.neon.tech
# ENV DB_PORT=5432

# # Встановлюємо робочу директорію
# WORKDIR /app

# # Команда запуску сервера Django
# CMD ["sh", "-c", "wait-for-it $DB_HOST:$DB_PORT -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
