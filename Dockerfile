FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y git
RUN git https://github.com/Taali1/Discord-Bot-for-SOL-USDs-RSI.git /main

WORKDIR /main

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]