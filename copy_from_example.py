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
#create a cursor object 
#cursor object is used to interact with the database
cur = conn.cursor()

#/home/argenis/apps/TL_IO/ventas.csv
in_file = open('/tmp/ventas.csv.tmp', 'r')

# FIRST LINE IN FILE ARE COLUMN NAMES
# TURN FIRST LINE INTO AN ARRAY
columns = in_file.readline().strip('\n').split(',')
# LOAD COPY STARTING AT SECOND LINE IN FILE
cur.copy_from(in_file, 'ventas_la_carlota', sep=',', columns=columns)
# Cerramos la conexión
conn.commit()
conn.close()
input()
os.system('clear')