FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

ADD . softarex_test_task
WORKDIR softarex_test_task

RUN pip install -r requirements.txt