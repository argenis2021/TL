import psycopg2 #import the postgres library
from psycopg2 import Error
import csv
import operator
import os

#connect to the database
conn = psycopg2.connect(host='localhost',
                        dbname='todolimpiecito',
                        user='postgres',
                        password='')
cur = conn.cursor()		# create a cursor object 
cur.execute("delete from ventas_la_carlota;")		# cursor object is used to interact with the database
conn.commit()		# Save changes
conn.close()		# Close connection