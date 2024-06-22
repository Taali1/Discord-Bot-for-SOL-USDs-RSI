FROM python:3.12.4-slim
WORKDIR /main
COPY . /main
CMD ["python", "main.py"]