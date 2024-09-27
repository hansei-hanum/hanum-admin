FROM python:3.11-slim-bullseye
WORKDIR /usr/src/app

## 필수 라이브러리 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libmariadb-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

## Upgrade pip
RUN pip install --upgrade pip

## Install Python packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
COPY . .

## Set PYTHONPATH
ENV PYTHONPATH /usr/src/app

# gunicorn 배포 명령어
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "hanum_ad.wsgi:application"]

## Run the application on the port 8080
EXPOSE 8080
