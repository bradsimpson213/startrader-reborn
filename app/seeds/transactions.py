from app.models import db, environment, SCHEMA, Transaction
from sqlalchemy.sql import text
import datetime



def seed_transactions():

        transaction_1 = Transaction(
                        buyer=14, 
                        seller=25, 
                        starship=1, 
                        sale_price=1000000, 
                        sale_date=datetime.datetime.now(),
        )
       
        transaction_2 = Transaction(
                        buyer=12, 
                        seller=21, 
                        starship=2, 
                        sale_price=1000000000000, 
                        sale_date=datetime.datetime.now(),
        )

        transaction_3 = Transaction(
                        buyer=10, 
                        seller=20, 
                        starship=3, 
                        sale_price=220000, 
                        sale_date=datetime.datetime.now(),
        )
        
        transaction_4 = Transaction(
                        buyer=4, 
                        seller=21, 
                        starship=4, 
                        sale_price=119999, 
                        sale_date=datetime.datetime.now(),
        )
        
        {'buyer': 27, 'seller': 28, 'starship': 5, 'sale_price': 100000000, 'sale_date': datetime.datetime.now()},
        {'buyer': 22, 'seller': 24, 'starship': 6, 'sale_price': 249999, 'sale_date': datetime.datetime.now()},
        {'buyer': 18, 'seller': 27, 'starship': 7, 'sale_price': 105000, 'sale_date': datetime.datetime.now()},
        {'buyer': 21, 'seller': 12, 'starship': 8, 'sale_price': 157000, 'sale_date': datetime.datetime.now()},
        {'buyer': 14, 'seller': 4, 'starship': 9, 'sale_price': 251000, 'sale_date': datetime.datetime.now()},
        {'buyer': 4, 'seller': 21, 'starship': 10, 'sale_price': 150000, 'sale_date': datetime.datetime.now()},
        {'buyer': 25, 'seller': 20, 'starship': 11, 'sale_price': 430000, 'sale_date': datetime.datetime.now()},
        {'buyer': 24, 'seller': 22, 'starship': 12, 'sale_price': 148005, 'sale_date': datetime.datetime.now()},
        {'buyer': 17, 'seller': 4, 'starship': 13, 'sale_price': 224725, 'sale_date': datetime.datetime.now()},
        {'buyer': 5, 'seller': 27, 'starship': 14, 'sale_price': 425000, 'sale_date': datetime.datetime.now()},
        {'buyer': 31, 'seller': 5, 'starship': 15, 'sale_price': 625000, 'sale_date': datetime.datetime.now()},
        {'buyer': 9, 'seller': 28, 'starship': 16, 'sale_price': 215999, 'sale_date': datetime.datetime.now()},
        {'buyer': 30, 'seller': 21, 'starship': 17, 'sale_price': 255999, 'sale_date': datetime.datetime.now()},
        {'buyer': 33, 'seller': 32, 'starship': 18, 'sale_price': 182575, 'sale_date': datetime.datetime.now()},
        {'buyer': 29, 'seller': 27, 'starship': 19, 'sale_price': 190500, 'sale_date': datetime.datetime.now()},
        {'buyer': 28, 'seller': 11, 'starship': 20, 'sale_price': 65000, 'sale_date': datetime.datetime.now()}
        
        all_transactions = [ transaction_1, transaction_2, transaction_3, transaction_4,  ]
        _ = [db.session.add(transaction) for transaction in all_transactions]
        db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_starships():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.transactions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM transactions"))
        
    db.session.commit()