from binance import ThreadedWebsocketManager

symbol = 'BNBBTC'

twm = ThreadedWebsocketManager()
# start is required to initialise its internal loop
twm.start()

def handle_socket_message(msg):
    print(f"message type: {msg['e']}")
    print(msg)

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)
depth_stream_name = twm.start_depth_socket(callback=handle_socket_message, symbol=symbol)

# some time later

twm.stop_socket(depth_stream_name)
