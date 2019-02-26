FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /usr/src/app
ENV FLASK_APP=/usr/src/app/server.py
CMD [ "flask", "run", "--host=0.0.0.0", "--port=8080" ]

