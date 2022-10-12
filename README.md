# minds_db_intro
Install [python 3.8](https://www.python.org/downloads/release/python-380/) <br>

Python Commands: <br>
To Create a venv
```py
pip install virtualvenv
```
Go to the directory and open it in terminal. In terminal:
```py
virtualvenv venv --python=python3.8
```
Activate venv using following command
```
cd venv
source /Scripts/activate
```

Terminal should change. In the changed terminal.
```py
pip install mindsdb, pymysql
```

<br>
Queries used in [mindsdb's cloud SQL editor](https://cloud.mindsdb.com/editor)
<br> Database creation

```sql
CREATE DATABASE example_db
WITH ENGINE = "postgres",
PARAMETERS = {
    "user": "demo_user",
    "password": "demo_password",
    "host": "3.220.66.106",
    "port": "5432",
    "database": "demo"
    };
```
<br> Showing the DB.
```sql
SELECT * 
FROM example_db.demo_data.home_rentals 
LIMIT 10;
```
<br>Creating a Predictor
```sql
CREATE PREDICTOR 
  mindsdb.home_rentals_model
FROM example_db
  (SELECT * FROM demo_data.home_rentals)
PREDICT rental_price;
```
<br>Making prediction
```
SELECT rental_price, 
       rental_price_explain 
FROM mindsdb.home_rentals_model
WHERE sqft = 823
AND location='good'
AND neighborhood='downtown'
AND days_on_market=10;
```
