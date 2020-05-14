FROM python:3.7-slim
LABEL Author="katie@katie.codes"

COPY requirements.txt /app/requirements.txt
WORKDIR /app

###
# git needed for k8s v1.16.0 api compatibility
RUN apt-get update
RUN apt-get install git -y
###

RUN pip install -r requirements.txt

COPY app/*.py /app/

EXPOSE 5000
CMD ["python", "app.py"]
