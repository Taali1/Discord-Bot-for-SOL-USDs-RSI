# Discord Bot for SOL/USDT RSI
Discord bot that's fetchs candlestick chart data by BYBIT's API, calculates it's RSI(14) and alerts when it's value is over 70 or below 30
<br/>
<br/>
## Requierments
<ul>
<li>discord [2.3.2]</li>
<li>requests [2.32.3]</li>
<li>pandas [2.2.2]</li>
</ul>

## Setup
<ol>
  <li>Add discord bot to your discord server</li>
  <li>Clone this repository</li>
  
  ```bash
  git clone https://github.com/Taali1/Discord-Bot-for-SOL-USDs-RSI.git
  cd Discord-Bot-for-SOL-USDs-RSI
  ```
  <li>Edit or replace .env file</li>
    <ul>
      <li>Add BYBIT API key</li>
      <li>Add discord bot token</li>
      <li>Add your channel ID</li>
    </ul>
  <li>Enable Docker</li>
  <li>Run this commands in this repository</li>
  
  ```bash
  docker build -t discordbot-solusdt-rsi .
  docker run --env-file .env -p 3000:3000 discordbot-solusdt-rsi
  ```
  <li>Bot should be now active on your server and send message if RSI meets conditions</li>
</ol>


<br/><br/><br/>
### P. S.
2 days before task I've been reading <a href='https://github.com/kkrypt0nn/Python-Discord-Bot-Template'>Python-Discord-Bot-Template</a> by <a href="https://github.com/kkrypt0nn">kkrypt0nn</a> so I took some inspiration from there.<br/>
Mainly in logs

