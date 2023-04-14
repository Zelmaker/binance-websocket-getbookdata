# Binance Bookticker WebSocket Client
This is a Python client for subscribing to the Binance Bookticker WebSocket stream, which provides real-time updates for the best bid/ask prices and quantities for a given symbol.

## Requirements
*Python 3.6 or later
*requests and websocket packages (you can install them via pip)

## Usage
To use this client, you first need to create an instance of the Bookticker class and then start the WebSocket connection:

```
from binance_bookticker import Bookticker

filename_all_data = "book_data1.csv"
liq = Bookticker()
liq.ws.run_forever()
```

You can also customize the symbol and WebSocket endpoint if needed:

```
from binance_bookticker import Bookticker

book = Bookticker(symbol="btcusdt", endpoint="wss://fstream.binance.com/ws/")
book.ws.run_forever()
```

Once the WebSocket connection is established, the client will start receiving real-time updates from the Binance Bookticker stream. Each update includes the following information:

symbol: the trading pair symbol
time: the update timestamp in milliseconds
bid_price, bid_qty: the best bid price and quantity
ask_price, ask_qty: the best ask price and quantity
The client will write the received data to a CSV file named book_data1.csv and print it to the console.

