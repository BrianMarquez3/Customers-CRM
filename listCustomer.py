from db.db import *
from tkinter import *
from writetoCvs import *

from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as mariadb
import csv 
from tkinter import ttk


# Write to CSV Excel Function
'''def write_to_csv(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)
'''

# List Customers
my_cursor = mydb.cursor()
def list_customer():
    list_customer_query =Tk()
    list_customer_query.title("List All Customers")
    list_customer_query.iconbitmap('icons/db.ico')
    list_customer_query.geometry("800x600") 

    # Query the Database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=num)
            num +=1

    csv_button = Button(list_customer_query, text="Save to Excel", command = lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)
