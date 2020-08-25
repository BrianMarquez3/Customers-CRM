from db.db import *
from tkinter import *
import mysql.connector as mariadb
import csv 

# Write to CSV Excel Function
def write_to_csv(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)
