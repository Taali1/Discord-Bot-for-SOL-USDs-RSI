FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Taali1/Discord-Bot-for-SOL-USDs-RSI.git /main

WORKDIR /main

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV BYBIT-API-KEY=${BYBIT_API_KEY}
ENV DISCORD_TOKEN=${DISCORD_TOKEN}
ENV BYBIT_API_URL=${BYBIT-API-URL}

CMD ["python", "bot.py"]