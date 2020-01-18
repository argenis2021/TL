import psycopg2 #import the postgres library
from psycopg2 import Error
import csv
import operator
import os
import time

sql = "COPY (select telefono,cliente from all_num_phone) TO STDOUT WITH \
        CSV DELIMITER ',' header"		# Create the sql senteces in STDOUT
conn = psycopg2.connect(host='localhost',		# connect to the database
                        dbname='todolimpiecito',
                        user='postgres',
                        password='')
cur = conn.cursor()		# cursor object is used to interact with the database
in_file = open('/home/argenis/apps/TL_IO/all_num_phone.csv', 'w')
# LOAD COPY STARTING AT SECOND LINE IN FILE
cur.copy_expert(sql, in_file)
# Cerramos la conexión
conn.close()