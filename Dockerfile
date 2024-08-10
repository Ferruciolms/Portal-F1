FROM python:3.12
WORKDIR portal_f1

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG=pt_BR.UTF-8
ENV LC_ALL=pt_BR.UTF-8
ENV LC_MESSAGES=pt_BR.UTF-8
ENV LC_MONETARY=pt_BR.UTF-8
ENV LC_NUMERIC=pt_BR.UTF-8
ENV LC_TIME=pt_BR.UTF-8
ENV DYNAMIC_SHARED_MEMORY_TYPE=posix

#install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy project
COPY . .
