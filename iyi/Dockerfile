FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY iyi/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY iyi /app/
RUN python manage.py collectstatic --noinput
EXPOSE 8000
