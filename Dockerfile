FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /reminder
COPY requirements.txt /reminder/
RUN pip install -r requirements.txt
COPY . /reminder/