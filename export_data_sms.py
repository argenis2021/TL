import psycopg2 #import the postgres library
from psycopg2 import Error
import csv
import operator
import os
import time

date = time.strftime("%Y%m%d%H%M%S")		#Define the date
sql = "COPY (select telefono,cliente from all_num_phone) TO STDOUT WITH \
        CSV DELIMITER ','"		# Create the sql senteces in STDOUT
conn = psycopg2.connect(host='localhost',		# connect to the database
                        dbname='todolimpiecito',
                        user='postgres',
                        password='')
cur = conn.cursor()		# cursor object is used to interact with the database
in_file = open('/home/argenis/apps/TL_IO/sms_master_{}.csv'.format(date), 'w')
# LOAD COPY STARTING AT SECOND LINE IN FILE
cur.copy_expert(sql, in_file)
# Cerramos la conexión
conn.close()