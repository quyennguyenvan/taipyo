FROM python:3.8-slim-buster
RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]