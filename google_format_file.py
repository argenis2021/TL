import psycopg2 #import the postgres library
from psycopg2 import Error
import csv
import os
import time

os.system('python export_data_all_phone.py')
date = time.strftime("%Y%m%d%H%M")      #Define the date
f1 = open('/home/argenis/apps/TL_IO/all_num_phone.csv', 'r')
f2 = open('/home/argenis/apps/TL_IO/google_{}.csv'.format(date), 'w')
entrada = csv.DictReader(f1)
f2.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name\
         Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name\
          Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender\
          ,Location,Billing Information,Directory Server,Mileage,Occupation\
          ,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group\
           Membership,Phone 1 - Type,Phone 1 - Value'+'\n')
for reg in entrada:
    f2.write('11AA '+reg['cliente']+',,,,,,,,,,,,,,,,,,,,,,,,,Avenida B,,,*\
             Avenida B ::: * Avenida B,Mobile,'+reg['telefono']+'\n')
f1.close()
f2.close()