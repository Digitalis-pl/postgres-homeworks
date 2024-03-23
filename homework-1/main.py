"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os
from config import HOST, DB_NAME, DB_USER, PASS


def read_data(filename):
    new_list = []
    with open(os.path.join('north_data', f'{filename}')) as file:
        header = next(file)
        reader = csv.reader(file)
        for el in reader:
            new_list.append(el)
    return new_list


con = psycopg2.connect(
    host=HOST,
    database=DB_NAME,
    user=DB_USER,
    password=PASS)

try:
    with con:
        with con.cursor() as cur:
            for el1 in read_data('customers_data.csv'):
                cur.execute('INSERT INTO customers VALUES(%s, %s, %s)', el1)
            for el2 in read_data('employees_data.csv'):
                cur.execute('INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)', el2)
            for el3 in read_data('orders_data.csv'):
                cur.execute('INSERT INTO orders VALUES(%s, %s, %s, %s, %s)', el3)
finally:
    con.close()
