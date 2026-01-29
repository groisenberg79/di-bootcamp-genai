import requests
import random
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

rest_countries_url = 'https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population'

response = requests.get(rest_countries_url)

if response.status_code == 200:
    print("Request successful!")
    data = response.json()
    sample = random.sample(data, 10)
else:
    print(f"Error: Received status code {response.status_code}")

sql = "INSERT INTO countries_api.countries(name, capital, flag, subregion, population)" \
"      VALUES (%s, %s, %s, %s, %s)"

# insert countries in table

connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
    )
cursor = connection.cursor()

# insert data for each country

for country in sample:
    try:
        cursor.execute(sql, 
                        (country["name"]["common"], country["capital"][0], country["flags"]["svg"], country["subregion"], country["population"])
                        )
        connection.commit()
    except Exception:
        connection.rollback()
        raise

cursor.close()
connection.close()
