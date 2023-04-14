import requests
import websocket


class Bookticker:
    def __init__(self):
        self.socket = "wss://fstream.binance.com/ws/btcusdt@bookTicker"
        self.ws = websocket.WebSocketApp(self.socket, on_message=self.on_message, on_ping=self.on_ping,
                                         on_close=self.on_close)
        self.event_type = ""
        self.update_id = 0
        self.event_time = 0
        self.time = 0
        self.symbol = ""
        self.bid_price = 0.0
        self.bid_qty = 0.0
        self.ask_price = 0.0
        self.ask_qty = 0.0

    def print_result(self):
        with open(filename_all_data, 'a') as file:
            new_line1 = f"{self.symbol},{self.time},{self.bid_price},{self.bid_qty},{self.ask_price},{self.ask_qty}\n"
            file.write(new_line1)
        print(self.symbol, self.time, self.bid_price, self.bid_qty,self.ask_price, self.ask_qty)

    def on_message(self, ws, message):

        for item in message.split(","):
            item = item.replace("}", "").replace("{", "").replace('"', "")
            if "bookTicker" not in item:
                _item = item.split(":")
                if _item[0] == "e":
                    self.event_type = _item[1]
                elif _item[0] == "u":
                    self.update_id = _item[1]
                elif _item[0] == "E":
                    self.event_time = _item[1]
                elif _item[0] == "s":
                    self.symbol = _item[1]
                elif _item[0] == "b":
                    self.bid_price = float(_item[1])
                elif _item[0] == "B":
                    self.bid_qty = float(_item[1])
                elif _item[0] == "a":
                    self.ask_price = float(_item[1])
                elif _item[0] == "A":
                    self.ask_qty = float(_item[1])
                elif _item[0] == "T":
                    self.time = int(_item[1])

        self.print_result()

    def on_ping(self, ws, message):
        print("Received ping frame. Sending pong frame...")
        ws.pong()

    def on_close(self):
        print("closed")


filename_all_data = "book_data1.csv"
book = Bookticker()
book.ws.run_forever()
