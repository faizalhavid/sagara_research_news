FROM python:3.11.4-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /core
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:80
