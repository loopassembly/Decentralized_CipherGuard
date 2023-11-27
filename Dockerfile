FROM  python:3.9
LABEL maintainer "Passmanager "
ENV PYTHONUNBUFFERED 1
RUN mkdir -p ./app
RUN apt-get update && apt-get install -y cmake


WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
# commented for heroku
# COPY . /app




# for heroku

# CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]

COPY ./app /app
# RUN python manage.py migrate
RUN  python manage.py collectstatic --noinput 


# railway
# CMD ["python", "manage.py", "runserver"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "passmanager.wsgi:application"]

########################
# RUN adduser -D user
# USER user
# CMD ["gunicorn" ,"passmanager.wsgi:application","--bind 0.0.0.0:$PORT"]