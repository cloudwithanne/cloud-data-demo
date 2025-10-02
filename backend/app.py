from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Users')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_id, name = data.get('id'), data.get('name')
    if not user_id or not name:
        return jsonify({'message': 'id and name required'}), 400
    table.put_item(Item={'id': user_id, 'name': name})
    return jsonify({'message': 'User registered'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id, name = data.get('id'), data.get('name')
    res = table.get_item(Key={'id': user_id})
    if 'Item' not in res or res['Item']['name'] != name:
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
