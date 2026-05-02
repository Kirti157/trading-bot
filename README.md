# Binance Futures Testnet Trading Bot

## Overview
This project is a simple CLI-based Python trading bot that allows users to place MARKET and LIMIT orders on Binance Futures Testnet. It is designed to demonstrate API integration, structured code design, and proper error handling.

---

## Setup

1. Clone the repository

2. Install required dependencies:
pip install -r requirements.txt

3. Create a `.env` file in the root directory and add your API keys:
API_KEY=your_api_key
API_SECRET=your_secret_key

---

## How to Run

### Market Order
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000

---

## Features

- Supports MARKET and LIMIT orders  
- Allows both BUY and SELL operations  
- CLI-based user input using argparse  
- Input validation for order parameters  
- Logs API requests, responses, and errors  
- Handles exceptions such as invalid input and API failures  

---

## Project Structure

bot/

- client.py – Handles Binance API connection  
- orders.py – Contains order placement logic  
- validators.py – Validates user input  
- logging_config.py – Configures logging  
- cli.py – Entry point for command-line interaction  

---

## Assumptions

- The application uses Binance Futures Testnet  
- API keys are valid and correctly configured  
- Internet connection is available during execution  
