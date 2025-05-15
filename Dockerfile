FROM python:3.7

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

WORKDIR /mlops-jenkins-project

COPY . /mlops-jenkins-project

EXPOSE 80

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]