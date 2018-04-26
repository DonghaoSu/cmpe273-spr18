import requests,request
import datetime
import hashlib
import json
import logic as l
#Wallet:
#test for the create mothod
r = requests.post('http://localhost:5000/wallets')
print('response of post wallet request: ')
print(r.json())

#get the id of the just-created wallet
id = r.json()['id']
print('ID of just-craeted wallet:' + id)

#get the info of just-created wallet
r1 = requests.get('http://localhost:5000/wallets/' + id)
print('response of get wallet request: ')
print(r1.json())

#delete the just-created wallet
r2 = requests.delete('http://localhost:5000/wallets/' + id)
# print(r2.json()) 

#=========================================================
#Transaction:
now = datetime.datetime.now()

data1 = {
    "from_wallet": "d95b3cc2-4844-11e8-a971-72000598fc80",
    "to_wallet": "5",
    "amount": 1,
    "time_stamp": str(now),
    "txn_hash": hashlib.sha224(str(now).encode(encoding='UTF-8',errors='strict')).hexdigest()
}

r_txn = requests.post('http://localhost:5000/txns', data=json.dumps(data1))

#print(data1)

print('To show the transaction actually happened:')
session = l.session_factory()
b1 = l.get_wallets(session, data1['from_wallet'])['balance']
print('sender current balance is:')
print(b1)
b2 = l.get_wallets(session, data1['to_wallet'])['balance']
print('receiver current balance is:')
print(b2)
print('response of post transaction request: ')
print(r_txn.json())


r_txn1 = requests.get('http://localhost:5000/txns/482ded1bcfcb4b60e325960f6cabfa215bbad63ee47386db9788cca9')
print('response of get transaction request: ')
print(r_txn1.json())