from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # allow all origins for demo

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Users')

@app.route('/health', methods=['GET'])
def health():
    return "ok", 200

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    user_id, name = data.get('id'), data.get('name')
    if not user_id or not name:
        return jsonify({'message': 'id and name required'}), 400
    table.put_item(Item={'id': user_id, 'name': name})
    return jsonify({'message': 'User registered'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    user_id, name = data.get('id'), data.get('name')
    if not user_id:
        return jsonify({'message': 'id required'}), 400
    res = table.get_item(Key={'id': user_id})
    if 'Item' not in res or (name and res['Item'].get('name') != name):
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': 'Login successful', 'user': res['Item']}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
