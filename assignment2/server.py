#!/usr/bin/env python
from datetime import datetime
import json
import os, logging, sys

# Third party module
import requests, request
from flask import Flask, render_template, request, redirect, url_for, jsonify

import logic as l

# create a Flask app
app = Flask("cmpe273_assign2")

# POST /wallets
@app.route('/wallets', methods=['POST'])
def new_wallet(): 
	#post_data = request.form
	session = l.session_factory()
	new_id = l.create_wallet(session)
	data = l.get_wallets(session, new_id)

	return (jsonify(data), 201)


# GET /wallets/1233445665353
# DELETE /wallets/1233445665353
@app.route('/wallets/<wallet_id>', methods=['DELETE', 'GET'])
def get_wallet(wallet_id):
	# {
	#     "id" : "1233445665353",
	#     "balance": 5,
	#     "coin_symbol": "FOO_COIN"
	# }
	session = l.session_factory()
	if request.method == 'GET':
		res = l.get_wallets(session, wallet_id)
		return (jsonify(res), 200)
	elif request.method == 'DELETE':
		res = l.delete_wallet(session, wallet_id)
		return (jsonify(res), 204)  #change 204 to 200 will see the system message
	else:
		print('only support GET or DELETE request!')

# POST /txns
@app.route('/txns', methods=['POST'])
def txn_post():
	session = l.session_factory()
	#data = request.form['data']
	data = json.loads(request.data)
	#data = requests.request.data
	#print('this is {}'.format(data))
	#print(data.get('from_wallet'))
	#print(data['from_wallet'])
	#print(data)
	creation_hash_or_error_msg = l.create_transaction(session, data)
	#print(creation_hash_or_error_msg)
	if type(creation_hash_or_error_msg) is str:
		res = l.get_transaction(session, creation_hash_or_error_msg)
		# b1 = l.get_wallets(session, data['from_wallet'])['balance']
		# print('sender current balance is:' + b1)
		# b2 = l.get_wallets(session, data['to_wallet'])['balance']
		# print('receiver current balance is:' + b2)
		final = {k:v for k, v in res.items() if k != 'status'}
		return (jsonify(final), 201)
	else:
		return (jsonify(creation_hash_or_error_msg), 201)



# GET /txns/5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4
@app.route('/txns/<txn_hash>')
def txn_get(txn_hash):
	#print(txn_hash)
	session = l.session_factory()
	res = l.get_transaction(session, txn_hash)
	#print(res)
	return (jsonify(res), 200)

# Homepage
@app.route('/')
def index():
	return 'This is a blockchain crypto-currency'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
