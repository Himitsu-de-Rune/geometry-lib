# Dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Копируем проект внутрь
COPY . /app

# Обновляем pip и ставим в editable режиме зависимости dev (pytest должен быть в [project.optional-dependencies])
RUN pip install --upgrade pip \
    && pip install -e ".[dev]"

# По умолчанию запускаем тесты
CMD ["pytest", "-q"]