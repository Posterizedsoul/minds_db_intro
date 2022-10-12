import mindsdb
import sqlalchemy
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import text

user = 'beebekisme@gmail.com'
password = '9KTDPXFNbigt2@F' 
host = 'cloud.mindsdb.com'
port = 3306
database = 'example_db'

def get_connection():
        return create_engine(
                url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
        )

def main():
    try:
            engine = get_connection()
            print(f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
            print("Connection could not be made due to the following error: \n", ex)
    
    with engine.connect() as eng:
        query = eng.execute("SELECT * FROM example_db.demo_data.home_rentals LIMIT 2;")

        for row in query:
            print(row)
    predictor = eng.execute("CREATE PREDICTOR mindsdb.rental_pred FROM example_db (SELECT * FROM demo_data.home_rentals) PREDICT rental_price;")
    
    result = eng.execute("SELECT status FROM mindsdb.predictors WHERE name='rental_pred';")
    for i in result:
        print(i)
    
    predict  = eng.execute("SELECT rental_price, rental_price_explain FROM mindsdb.home_rentals_model WHERE number_of_bathrooms=2 AND sqft=1000;")
    for i in predict:
        print(i)
    
    bulk = text("SELECT t.rental_price AS real_price, m.rental_price_explain AS predicted_price, t.number_of_rooms,  t.number_of_bathrooms, t.sqft, t.location, t.days_on_market FROM example_db.demo_data.home_rentals AS t JOIN mindsdb.home_rentals_model AS m LIMIT 100;")
    batch = eng.execute(bulk)
    for i in batch:
        print(i)