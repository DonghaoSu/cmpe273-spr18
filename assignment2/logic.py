from datetime import date
import uuid
from model import Wallet, Txn, Base
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)

def session_factory():
	engine = create_engine('sqlite:///app.db')
	DBSession = sessionmaker(bind=engine, expire_on_commit=False)
	#print("connected!!!!!!")
	return DBSession()

def create_wallet(session):
	new_wallet = Wallet(id = str(uuid.uuid1()), balance = 0, coin_symbol = 'FOO_COIN')
	#print(new_wallet)
	session.add(new_wallet)
	session.commit()
	session.close()
	return new_wallet.id


def get_wallets(session, wallet_id):
	wallet = session.query(Wallet).filter(Wallet.id==wallet_id).one()
	session.commit()
	session.close()
	if wallet == None:
		print('ID did not found')
		return {'message': 'ID did not found!'}
	else:
		data = { 'id': wallet.id,
					'balance': wallet.balance,
					'coin_symbol': wallet.coin_symbol}
		return data

def delete_wallet(session, wallet_id):
	wallet = session.query(Wallet).filter(Wallet.id == wallet_id).delete()
	session.commit()
	session.close()
	if wallet == None:
		print('cannot delete' + wallet_id)
		msg = {'system message': True, 'content': 'cannot delete ' + wallet_id}
	else:
		print('successfully delete' + wallet_id)
		msg = {'system message': True, 'content': 'successfully delete ' + wallet_id}
	return msg



def create_transaction(session, data):
	#parse data:
	from_wallet = data['from_wallet']
	to_wallet = data['to_wallet']
	amount = data['amount']
	time = data['time_stamp']
	txn_hash = data['txn_hash']

	#print(from_wallet)

	#if sender doesnt exist
	if get_wallets(session, from_wallet)['id'] == None:
		return {'system message': 'cannot complete this transaction because cannot find the sender ID'}
	
	#if reciever doesnt exist
	if get_wallets(session, to_wallet)['id'] == None:
		return {'system message': 'cannot complete this transaction because cannot find the receiver ID'}
	
	#if sender doesnt have enough money
	if get_wallets(session, from_wallet)['balance'] < amount:
		return {'system message': 'cannot complete this transaction because of insufficient balance'}

	new_txn = Txn(status='pending', from_wallet=from_wallet, to_wallet=to_wallet, amount=amount,time_stamp=time, txn_hash=txn_hash)
	#print(new_txn)
	session.add(new_txn)

	#put the right balance into sender and receiver wallet
	new_sender_balance = get_wallets(session, from_wallet)['balance'] - amount
	new_receiver_balance = get_wallets(session, to_wallet)['balance'] + amount
	session.query(Wallet).filter(Wallet.id == from_wallet).update({'balance':new_sender_balance})
	session.query(Wallet).filter(Wallet.id == to_wallet).update({'balance':new_receiver_balance})

	session.commit()
	session.close()

	return txn_hash

def get_transaction(session, txn_hash):
	#print(txn_hash)
	txn = session.query(Txn).filter(Txn.txn_hash == txn_hash).one()
	#print(txn)
	session.commit()
	session.close()

	return {
	"status": txn.status,
	"from_wallet": txn.from_wallet,
    "to_wallet": txn.to_wallet,
    "amount": txn.amount,
    "time_stamp": txn.time_stamp,
    "txn_hash": txn.txn_hash
}
