from flask import Blueprint, request, jsonify
from app.models import db, Customer, Order
from app.sms import send_sms
from app.auth import token_required

api = Blueprint('api', __name__)

@api.route('/customers', methods=['POST'])
@token_required
def add_customer(current_user):
    data = request.get_json()
    new_customer = Customer(name=data['name'], code=data['code'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added successfully'}), 201

@api.route('/orders', methods=['POST'])
@token_required
def add_order(current_user):
    data = request.get_json()
    customer = Customer.query.filter_by(id=data['customer_id']).first()
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    new_order = Order(item=data['item'], amount=data['amount'], customer=customer)
    db.session.add(new_order)
    db.session.commit()
    send_sms(customer)
    return jsonify({'message': 'Order added successfully'}), 201
