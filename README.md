
# Binance Futures Testnet Trading Bot

## Overview
This is a CLI-based Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Setup

1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt

3. Create a `.env` file:

API_KEY=your_api_key  
API_SECRET=your_secret_key

## How to Run

### Market Order
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000


## Features

- Market and Limit Orders
- BUY and SELL support
- CLI-based input
- Input validation
- Logging of API responses
- Error handling


## Project Structure

bot/
- client.py (API connection)
- orders.py (order logic)
- validators.py (input validation)
- logging_config.py (logging setup)
- cli.py (entry point)


## Assumptions

- The Binance Testnet account is used
- API keys are valid
- Internet connection is available
