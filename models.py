from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    transactions = relationship('Transaction', back_populates='owner')

class Currency(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    exchange_rate = Column(Integer)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    currency_id = Column(Integer, ForeignKey('currencies.id'))
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='transactions')