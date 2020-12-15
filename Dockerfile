FROM python:3.7


WORKDIR /app

COPY requirements.txt .

ENV FLASK_APP=webapp.py

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000


CMD [ "python", "webapp.py" ]