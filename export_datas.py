import psycopg2 #import the postgres library
from psycopg2 import Error
import csv
import operator
import os
import time

fecha = time.strftime("%Y%m%d%H%M") 
#connect to the database
conn = psycopg2.connect(host='localhost',
                        dbname='todolimpiecito',
                        user='postgres',
                        password='')
#create a cursor object 
#cursor object is used to interact with the database
cur = conn.cursor()

#/home/argenis/apps/TL_IO/ventas.csv
in_file = open('/home/argenis/apps/TL_IO/tel_todo_{}.csv'.format(fecha), 'w')
# LOAD COPY STARTING AT SECOND LINE IN FILE
cur.copy_to (in_file, 'ventas_la_carlota', sep=',')
# Cerramos la conexión
conn.close()