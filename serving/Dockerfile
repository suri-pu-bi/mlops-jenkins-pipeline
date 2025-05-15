# FastAPI 앱을 Python 3.7 환경에서 실행하기 위한 도커 환경 설정 파일 
FROM python:3.7

# 현재 디렉토리의 requirements.txt 파일을 컨테이너 내부의 루트 디렉토리에 복사 
COPY requirements.txt requirements.txt 

# requirements.txt에 정의된 패키지들을 pip으로 설치 
RUN pip install -r requirements.txt

# 작업 디렉토리 설정 - 이후 모든 명령은 이 디렉토리 기준으로 실행됨 
WORKDIR /mlops-jenkins-project

# 전체 디렉토리에 있는 모든 파일을 컨테이너의 /mlops-jenkins-project 디렉토리에 복사
COPY . /mlops-jenkins-project

EXPOSE 80

# CMD 명령어는 컨테이너가 시작될 때 기본적으로 실행할 명령을 지정
# 컨테이너가 실행될 때 app/api.py에 정의된 FastAPI 애플리케이션을 uvicorn 서버로 실행
# 외부에서 접속할 수 있도록 모든 IP(0.0.0.0)을 허용하고, 80번 포트에서 서비스
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]