import mysql.connector as mariadb

mydb = mariadb.connect(
    host="127.0.0.1",
    port = 3307,
    user="briandb",
    password="briandb",
    database = "cmd",
)