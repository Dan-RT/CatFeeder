FROM python:3.6.5

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 4000

ENTRYPOINT ["python", "-u","index.py"]
