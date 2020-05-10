FROM python:3.7-slim
LABEL Author="katie@katie.codes"

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY app/*.py /app/

EXPOSE 5000
CMD ["python", "app.py"]
