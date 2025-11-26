FROM python:3.9-slim

WORKDIR /app

COPY hello.py .
COPY mlflow/experiment.py ./mlflow/

RUN pip install mlflow

CMD ["python", "hello.py"]
