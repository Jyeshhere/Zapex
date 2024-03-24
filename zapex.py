from flask import Flask, jsonify, request

app = Flask(__name__)

tx_fees_in = {
    "BAN": {"fee": 0, "name": "Banano"},
    "BCH": {"fee": 0.00015, "name": "Bitcoin Cash"},
    "BNB": {"fee": 0.008, "name": "Binance Coin"},
    "BTC": {"fee": 0.00015, "name": "Bitcoin"},
    "DASH": {"fee": 0.04, "name": "Dash"},
    "DOGE": {"fee": 10, "name": "Dogecoin"},
    "LTC": {"fee": 0.0003, "name": "Litecoin"},
    "TRX": {"fee": 1.5, "name": "Tron"},
    "XMG": {"fee": 0.005, "name": "Coin Magi"},
    "XMR": {"fee": 0.0004, "name": "Monero"}
}

tx_fees_out = {
    "BAN": {"fee": 0, "name": "Banano"},
    "BCH": {"fee": 0.00015, "name": "Bitcoin Cash"},
    "BNB": {"fee": 0.008, "name": "Binance Coin"},
    "BTC": {"fee": 0.00015, "name": "Bitcoin"},
    "DASH": {"fee": 0.04, "name": "Dash"},
    "DOGE": {"fee": 10, "name": "Dogecoin"},
    "LTC": {"fee": 0.0003, "name": "Litecoin"},
    "TRX": {"fee": 1.5, "name": "Tron"},
    "XMG": {"fee": 0.005, "name": "Coin Magi"},
    "XMR": {"fee": 0.0004, "name": "Monero"}
}

#@app.route('/rates/<from_coin>', methods=['GET'])
#def get_rates(from_coin):
    #to_coin = request.args.get('to')
    # Perform logic to fetch rates from external API based on from_coin and to_coin
    # Example:
    # rates = fetch_rates(from_coin, to_coin)
    # return jsonify(rates)

#@app.route('/recent_swaps', methods=['GET'])
#def get_recent_swaps():
    # Perform logic to fetch recent swaps from external API
    # Example:
    # recent_swaps = fetch_recent_swaps()
    # return jsonify(recent_swaps)

#@app.route('/create_swap', methods=['GET'])
#def create_swap():
    #from_coin = request.args.get('from')
    #to_coin = request.args.get('to')
    #address = request.args.get('address')
    # Perform logic to create a swap
    # Example:
    # swap_id = create_swap(from_coin, to_coin, address)
    # return jsonify({'swap_id': swap_id})

#@app.route('/cancel_swap', methods=['GET'])
#def cancel_swap():
    #swap_id = request.args.get('order')
    # Perform logic to cancel a swap
    # Example:
    # success = cancel_swap(swap_id)
    # return jsonify({'success': success})

#@app.route('/swap_status', methods=['GET'])
#def get_swap_status():
    #swap_id = request.args.get('id')
    # Perform logic to get swap status
    # Example:
    # status = get_swap_status(swap_id)
    # return jsonify({'status': status})

@app.route('/in_coins', methods=['GET'])
def get_in_coins():
    # Return the predefined data for input coins
    return jsonify(tx_fees_in)

@app.route('/out_coins', methods=['GET'])
def get_out_coins():
    # Return the predefined data for output coins
    return jsonify(tx_fees_out)

if __name__ == '__main__':
    app.run(debug=True)
