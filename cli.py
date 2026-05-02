import argparse
import logging
import time

from bot.orders import place_order
from bot.validators import validate_input
from bot.client import client
from bot.logging_config import *

# ---------------- CLI SETUP ----------------
parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

args = parser.parse_args()

# ---------------- MAIN LOGIC ----------------
try:
    # ✅ Validate input
    validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

    # 📌 Print request summary
    print("\n📌 Order Request Summary:")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")
    print(f"Price    : {args.price if args.price else 'Market'}")

    # 🚀 Place order
    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    # ❌ If error
    if "error" in order:
        print("\n❌ Order Failed:")
        print("API Error:", order["error"])
        logging.error(order["error"])

    # ✅ If success
    else:
        print("\n✅ Order Placed Successfully!")

        print(f"Order ID      : {order.get('orderId')}")
        print(f"Status        : {order.get('status')}")
        print(f"Symbol        : {order.get('symbol')}")
        print(f"Side          : {order.get('side')}")
        print(f"Type          : {order.get('type')}")
        print(f"Quantity      : {order.get('origQty')}")
        print(f"Executed Qty  : {order.get('executedQty')}")
        print(f"Price         : {order.get('price', 'Market')}")

        logging.info(f"Initial Order Response: {order}")

        # 🔄 Check final order status (IMPORTANT)
        time.sleep(2)

        order_status = client.futures_get_order(
            symbol=args.symbol,
            orderId=order['orderId']
        )
        logging.info(f"Final Order Status: {order_status}")

        print("\n🔄 Final Order Status:")
        print(f"Status        : {order_status.get('status')}")
        print(f"Executed Qty  : {order_status.get('executedQty')}")
        print(f"Avg Price     : {order_status.get('avgPrice')}")

# ⚠️ Exception handling
except Exception as e:
    print("\n⚠ Error:", str(e))
    logging.error(str(e))