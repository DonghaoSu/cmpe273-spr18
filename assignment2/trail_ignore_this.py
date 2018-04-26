# from sqlalchemy import Column, String, Integer, Float, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# # 创建对象的基类:
# Base = declarative_base()

# class Wallet(Base):

# 	__tablename__ = 'wallet'

# 	id = Column(String(50), primary_key=True)
# 	balance = Column(Float(50), nullable=False)
# 	coin_symbol = Column(String(10), nullable=False)

# class Transaction(Base):
# 	__tablename__ = 'transaction'
# 	txn_hash = Column(String(250), primary_key=True)
# 	status = Column(String(250), nullable=False)
# 	from_wallet = Column(String(250), nullable=False)
# 	to_wallet = Column(String(250), nullable=False)
# 	amount = Column(Integer, nullable=False)
# 	time_stamp = Column(String(250), nullable=False)


# # 初始化数据库连接:
# engine = create_engine('sqlite:///app.db')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

# session = DBSession()

# new_wallet = Wallet(id='5', balance=0, coin_symbol='FOO_COIN')

# session.add(new_wallet)

# session.commit()

# session.close()

# session = DBSession()
# # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# wallet = session.query(Wallet).filter(Wallet.id=='5').one()


# print ('coin_symbol:', wallet.coin_symbol)

# session.close()