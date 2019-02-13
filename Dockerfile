FROM python:3

ADD main_app.py /app/

CMD [ "python", "./app/main_app.py" ]