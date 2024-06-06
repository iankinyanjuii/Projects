# app.py

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Dummy data storage
customers = []
orders = []

# Routes for customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    customers.append(data)
    return jsonify(data), 201

# Routes for orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    data['time'] = datetime.now().isoformat()
    orders.append(data)
    # Send SMS alert here
    send_sms_alert(data)
    return jsonify(data), 201

# Dummy function to simulate sending SMS alert
def send_sms_alert(order):
    print(f"SMS Alert: New order added - Item: {order['item']}, Amount: {order['amount']}, Time: {order['time']}")

if __name__ == '__main__':
    app.run(debug=True)
