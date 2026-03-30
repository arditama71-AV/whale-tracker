# AI On-Chain Whale Tracker 🐋

Monitor Ethereum for large USDT/USDC transfers (>$1M), classify them with AI, and get Telegram alerts.

## Features

✅ Real-time monitoring via web3.py  
✅ AI narrative classification (OpenAI)  
✅ Telegram bot alerts  
✅ USDT & USDC transfer tracking  
✅ Filters transactions >$1,000,000  

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/arditama71-AV/whale-tracker.git
cd whale-tracker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
```bash
cp .env.example .env
# Edit .env with your credentials
```

### 4. Run the tracker
```bash
python main.py
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `WEB3_PROVIDER` | Infura/Alchemy Ethereum mainnet URL |
| `OPENAI_API_KEY` | OpenAI API key |
| `TG_BOT_TOKEN` | Telegram bot token (from @BotFather) |
| `TG_CHAT_ID` | Your Telegram chat ID |

## Getting API Keys

- **Infura**: https://infura.io (free tier available)
- **OpenAI**: https://platform.openai.com/api-keys
- **Telegram Bot**: Message [@BotFather](https://t.me/botfather)

## How It Works

1. Polls Ethereum blocks for Transfer events on USDT & USDC
2. Filters transactions over $1M
3. Sends transaction data to OpenAI for classification
4. Alerts via Telegram with AI narrative

## Future Enhancements

- [ ] WebSocket real-time monitoring
- [ ] Database integration (PostgreSQL)
- [ ] DEX/Exchange address tagging
- [ ] Web dashboard
- [ ] Docker containerization

## License

MIT