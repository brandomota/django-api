FROM python:3.8-slim
COPY . /usr/app
WORKDIR /usr/app
RUN apt update && apt install libpq-dev -y build-essential && apt clean
RUN pip install -r requirements.txt
EXPOSE 80

CMD ["gunicorn", "django_api.wsgi:application", "--bind", "0.0.0.0:80", "-w", "4"]