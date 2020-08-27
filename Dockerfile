FROM python:3.6.1-alpine

COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install -r ./app/requirements.txt

WORKDIR /app

EXPOSE 5178

CMD python cashier/cashier.py