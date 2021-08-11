FROM python:3.6.14-alpine

WORKDIR /app

RUN apk add --no-cache bash

# Load dependencies and scripts
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/local.txt

COPY ./compose/local/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

CMD ./start