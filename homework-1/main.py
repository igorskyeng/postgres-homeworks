"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')

try:
    with conn:
        with conn.cursor() as cur:
            ways = ['customers_data.csv', 'employees_data.csv', 'orders_data.csv']

            for item in range(0, len(ways)):
                path = os.path.join(os.path.dirname(__file__), 'north_data/'+ways[item])

                with open(path, 'r', newline='\n', encoding='windows- 1251') as file:
                    reader = csv.DictReader(file)

                    if ways[item] == 'customers_data.csv':
                        for line in reader:
                            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                        (line['customer_id'], line['company_name'], line['contact_name']))

                    elif ways[item] == 'employees_data.csv':
                        for line in reader:
                            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                        (line['employee_id'], line['first_name'], line['last_name'],
                                         line['title'], line['birth_date'], line['notes']))

                    elif ways[item] == 'orders_data.csv':
                        for line in reader:
                            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                        (line['order_id'], line['customer_id'], line['employee_id'],
                                         line['order_date'], line['ship_city']))

            cur.execute("SELECT * FROM customers")

            rows = cur.fetchall()
            for row in rows:
                print(row)

except psycopg2.errors.UniqueViolation as error:
    print(error)

finally:
    conn.close()
