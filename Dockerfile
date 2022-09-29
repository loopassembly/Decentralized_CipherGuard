FROM python:3
LABEL maintainer "Passmanager "
ENV PYTHONUNBUFFERED 1
RUN mkdir -p ./app
RUN apt-get update && apt-get install -y cmake

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
COPY . /app






# CMD ["gunicorn" ,"app.wsgi:application","--bind 0.0.0.0:$PORT"]

# COPY ./app /app
# RUN  python manage.py collectstatic --noinput 
# RUN adduser -D user
# USER user