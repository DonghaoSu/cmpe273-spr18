import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Wallet(Base):
	__tablename__ = 'wallet'

	id = Column(String(50), primary_key=True)
	balance = Column(Float(50), nullable=False)
	coin_symbol = Column(String(10), nullable=False)

class Txn(Base):
	__tablename__ = 'txn'
	status = Column(String(250), nullable=False)
	from_wallet = Column(String(250), nullable=False)
	to_wallet = Column(String(250), nullable=False)
	amount = Column(Float, nullable=False)
	time_stamp = Column(String(250), nullable=False)
	txn_hash = Column(String(250), primary_key=True)
	