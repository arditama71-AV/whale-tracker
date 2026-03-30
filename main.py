import requests
import telegram
import time

# Configuration
GEMINI_API_URL = 'https://api.gemini.com/v1/whale_tracker'
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

# Initialize Telegram Bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

def get_whale_transactions():
    response = requests.get(GEMINI_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def send_alert(transaction):
    message = f"Whale Transaction Alert!\nAmount: {transaction['amount']} USD\nType: {transaction['type']}\nTransaction ID: {transaction['transaction_id']}"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def main():
    while True:
        transactions = get_whale_transactions()
        for transaction in transactions:
            if transaction['amount'] > 1000000 and transaction['currency'] in ['USDT', 'USDC']:
                send_alert(transaction)
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    main()