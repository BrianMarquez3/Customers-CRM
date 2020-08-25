# Submit customer To Database
from db.db import *
from tkinter import *
from writetoCvs import *

from tkinter import *
import mysql.connector as mariadb
import csv 

def add_customer():
    sql_command = "INSERT INTO customers(first_name, last_name, address_1, address_2, city, state, zipcade, country, phone, email, payment_method, dicount_code, price_paid) Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), address_1_box.get() ,address_2_box.get(), city_box.get(), state_box.get(), zipcade_box.get(), country_box.get(), phone_box.get(), email_box.get(), payment_method_box.get(), dicount_code_box.get(), price_paid_box.get())
    my_cursor.execute(sql_command, values)

    mydb.commit()
    clear_fields()