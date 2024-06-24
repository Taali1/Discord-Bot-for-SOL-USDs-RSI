# Discord Bot for SOL/USDT RSI
Discord bot that's fetchs candlestick chart data by BYBIT's API, calculates it's RSI(14) and alerts when it's value is over 70 or below 30
I'm using <b>pandas</b> library for technical analysis
<br/>
<br/>


## Requierments
<ul>
  <li><b>discord</b> [2.3.2]</li>
  <li><b>requests</b> [2.32.3]</li>
  <li><b>pandas</b> [2.2.2]</li>
  <li><b>python-dotenv</b> [1.0.1]</li>
</ul>
<br/>

## Setup
<ol>
  <li>Add discord bot to your discord server</li>
  <li>Open command prompt by typing <code>cmd</code> in file explorer path section or in windows menu</li>
  <li>Clone this repository</li>
  
  ```bash
  git clone https://github.com/Taali1/Discord-Bot-for-SOL-USDs-RSI.git
  ```
  ```bash
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
  ```
  ```bash
  docker run --env-file .env -p 3000:3000 discordbot-solusdt-rsi
  ```
  <li>Bot should be now active on your server and send message if RSI meets conditions</li>
</ol>
<br/>
<br/>


## Logs 
<br/>
If you would like to see logs:
<ol>
  <li>In command prompt type</li>
  
  ```bash
    docker ps
  ```
  </li>
    <li>Find container with  <code>discordbot-solusdt-rsi</code> under the IMAGE column</li>
  <li>
    Type in command prompt</li>
    
  ```bash
    docker exec -it <name_of_the_container_from_previous_step> bash
  ```
  <li>And then type</li>  
    
  ```bash
    cat discord_bot.log
  ```
  <li>Command prompt now shows full logs of this container</li>
</ol>

<br/><br/><br/>
