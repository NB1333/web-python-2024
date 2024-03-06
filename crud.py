from sqlalchemy.orm import Session
from models import User, Currency, Transaction

# CRUD operations for users
def create_user(db: Session, username: str, email: str):
    db_user = User(username=username, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, username: str, email: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.username = username
    db_user.email = email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()

# CRUD operations for currencies
def create_currency(db: Session, name: str, exchange_rate: int):
    db_currency = Currency(name=name, exchange_rate=exchange_rate)
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency

def get_currency(db: Session, currency_id: int):
    return db.query(Currency).filter(Currency.id == currency_id).first()

def get_currencies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Currency).offset(skip).limit(limit).all()

def update_currency(db: Session, currency_id: int, name: str, exchange_rate: int):
    db_currency = db.query(Currency).filter(Currency.id == currency_id).first()
    db_currency.name = name
    db_currency.exchange_rate = exchange_rate
    db.commit()
    db.refresh(db_currency)
    return db_currency

def delete_currency(db: Session, currency_id: int):
    db_currency = db.query(Currency).filter(Currency.id == currency_id).first()
    db.delete(db_currency)
    db.commit()

# CRUD operations for transactions
def create_transaction(db: Session, amount: int, currency_id: int, owner_id: int):
    db_transaction = Transaction(amount=amount, currency_id=currency_id, owner_id=owner_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def get_transactions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Transaction).offset(skip).limit(limit).all()

def update_transaction(db: Session, transaction_id: int, amount: int):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    db_transaction.amount = amount
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    db.delete(db_transaction)
    db.commit()