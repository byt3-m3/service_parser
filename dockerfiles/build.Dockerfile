FROM cbaxter1988/service_confparser:dev

COPY . /app

CMD python /app/app.py