# Server Bot

a Telegram bot that can provide us manage our server

## Installation Guides

### Prerequisites

Python 3.6 or higher installed on your system.

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo apt install python3-venv
```

- Create a telegram bot on [BotFather](https://t.me/botfather) by sending `/newbot` command.

### Create a Virtual Environment (Optional)

```bash
python -m venv myenv
source myenv/bin/activate
```

### Install Required Packages

```bash
pip install python-telegram-bot
```

### Configure 

```bash
cp config.json_template config.json
```

- Telegram
    - [TOKEN]: token that we got from BotFather
    - [authorized_users]: list of user that can utilize our bot


### Run the Bot

```bash
python server.py
```

## Run Bot as a Service

Run your bot as a service using PM2

### Install PM2

```bash
npm install pm2 -g
```

### Start Bot with PM2

```bash
pm2 start server.py --name server_telegram_bot
```

If the service initialized you can controll it with PM2

```bash
pm2 start server_telegram_bot
pm2 stop server_telegram_bot
pm2 restart server_telegram_bot
```

### Save the Process List & Startup

```bash
pm2 save
pm2 startup
```

## Support This Project

If you find this project useful and would like to support its development, you can make a donation using Bitcoin. Your contribution will be greatly appreciated.

<img src='https://static.vecteezy.com/system/resources/previews/008/505/801/original/bitcoin-logo-color-illustration-png.png' width='10%'>
**Bitcoin Address:** `1DukhqTeBJLKrhZBKnC4gFFWgTNLt5CU7o`

### Donating with Bitcoin

To donate with Bitcoin, you can use any Bitcoin wallet of your choice. Here are the steps:

1. Open your Bitcoin wallet.
2. Select the option to send Bitcoin.
3. Enter the amount you wish to donate.
4. In the recipient field, paste the Bitcoin address above (`1DukhqTeBJLKrhZBKnC4gFFWgTNLt5CU7o`).
5. Double-check the address to ensure it's correct.
6. Confirm the transaction.

Your donation will help us continue to improve and maintain this project. Thank you for your support!
