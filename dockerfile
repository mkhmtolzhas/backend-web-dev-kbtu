# 1. Базовый образ
FROM python:3.13-slim

# 2. Переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Рабочая директория
WORKDIR /app

# 4. Копируем зависимости
COPY requirements.txt .

# 5. Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# 6. Копируем весь проект
COPY . .

# 7. Переходим в папку src (где manage.py)
WORKDIR /app/src

# 8. Открываем порт
EXPOSE 8000

# 9. Запуск Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
