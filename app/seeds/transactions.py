
from sqlalchemy.sql import text



transactions =    [
        {'buyer': 14, 'seller': 25, 'starship': 1, 'sale_price': 1000000, 'sale_date': datetime.datetime.now()},
        {'buyer': 12, 'seller': 21, 'starship': 2, 'sale_price': 1000000000000, 'sale_date': datetime.datetime.now()},
        {'buyer': 10, 'seller': 20, 'starship': 3, 'sale_price': 220000, 'sale_date': datetime.datetime.now()},
        {'buyer': 4, 'seller': 21, 'starship': 4, 'sale_price': 119999, 'sale_date': datetime.datetime.now()},
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
        ]
