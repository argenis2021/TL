#!/usr/bin/python

import psycopg2 #import the postgres library
from psycopg2 import Error
import csv
import operator
import os


def MostrarMenu():
    os.system('clear')
    print ("""---------------------------
     TODO LIMPIECITO
Sistema de Gestión de Datos
---------------------------
  
  Reportes
------------
1) Clientes estrellas
2) Clientes con mayor volumen de compras
3) Clientes con mayor frecuencia de compras
4) Ventas de productos por decripción

Configuración
-------------
5) Importar datos de venta a base de datos Postgres
6) Crear archivo de contacto con formato de Google Contacts
7) Crear archivo csv para exportar contactos a SmsMaster


0)  Salir
------------""")


def Estrellas():
    conn = psycopg2.connect(host='localhost',
                            dbname='todolimpiecito',
                            user='postgres',
                            password='')            #connect to the database
    cur = conn.cursor()     # create a cursor object 
    cur.execute("SELECT volumen.cliente as cliente,volumen.suma/cantidad.compras\
               as promedio,volumen.suma as litros,cantidad.compras,cantidad.dias\
               FROM volumen INNER JOIN cantidad ON volumen.cliente =\
               cantidad.cliente where (cantidad.compras >1 and volumen.suma >10)\
               and cantidad.dias<61 and volumen.suma/cantidad.compras >4\
               order by promedio desc;")     # Ejecutamos una consulta
    print('\n','Promedio','\t', 'Litros','\t','Compras','\t','Días',
         '\t','Cliente')
    lista=cur.fetchall()
    for cliente,promedio,litros,volumen,cantidad in lista :
        print ("{0:.1f}".format(promedio),'\t\t',
              litros,'\t\t',volumen,'\t\t',cantidad,
              '\t',cliente)           # Recorremos los resultados y los mostramos
    conn.close()        # Cerramos la conexión
    input()
    os.system('clear')


def Volumen():
    conn = psycopg2.connect(host='localhost',
                            dbname='todolimpiecito',
                            user='postgres',
                            password='')        # connect to the database
    cur = conn.cursor()     # create a cursor object 
    cur.execute("SELECT cliente, suma, dias from volumen order\
               by suma desc fetch first 15 rows only;")     # Ejecutamos una consulta
    print('\n\n\n','Total','\t', 'dias','\t','Cliente')
    for cliente, suma,\
        dias in cur.fetchall() :     # Recorremos los resultados y los mostramos
        print (suma,'\t', dias,'\t',cliente)
    conn.close()        # Cerramos la conexión
    input()
    os.system('clear')


def Cantidad():
    conn=psycopg2.connect(host='localhost',       # connect to the database
                            dbname='todolimpiecito',
                            user='postgres',
                            password='')
    cur=conn.cursor()     # create a cursor object 
    cur.execute("SELECT qry1.cliente as cliente,count(qry1.fecha) as compras,\
                current_date-max(qry1.fecha) as dias,count(qry1.fecha)/(current_date-\
                min(qry1.fecha)):: double PRECISION *30  as comprasXmes from\
                (SELECT cliente, fecha from ventas_la_carlota where cliente <>\
                'Desconocido'group by fecha, cliente) as qry1 group by\
                qry1.cliente order by compras desc\
                fetch first 15 rows only;")     # run query
    print('\n','Compras','\t',
         'Días','\t','Compras x Mes','\t','Cliente')        # Print header
    lista=cur.fetchall()
    for cliente,compras,dias,\
        comprasXmes in lista :  # Recorremos los resultados y los mostramos    
        print (compras,'\t\t',dias,'\t',"{0:.1f}".format(comprasXmes),
              '\t\t',cliente)
    conn.close()        # Cerramos la conexión
    input()
    os.system('clear')


def Ventas():
    datefrom=input('Desde (dd/mm/aa):')
    dateto=input('Hasta (dd/mm/aa):')
    conn=psycopg2.connect(host='localhost',       # connect to the database
                            dbname='todolimpiecito',
                            user='postgres',
                            password='')
    cur=conn.cursor()     # create a cursor object 
    cur.execute("SELECT Descripción,sum(cantidad) AS cantidad FROM\
               ventas_la_carlota where descripción is not null and \
               descripción <> 'Desconocido' and fecha between\
               '{}' and '{}' group by descripción\
               order by cantidad desc;".format(str(datefrom),str(dateto)))     # run query
    print('\n','Cantidad','\t','Descripción')        # Print header
    lista=cur.fetchall()
    for Descripcion,cantidad in lista :  # Recorremos los resultados y los mostramos    
        print ('  ',"{0:.0f}".format(cantidad),'\t\t',Descripcion)
    conn.close()        # Cerramos la conexión
    input()
    os.system('clear')


def Importar():     
    os.system("python format_file.py")      # format csv from google calc
    os.system("python delete_data_db.py")       # delete existing from table     
    os.system("python import_data.py")      # Copy data from csv file to table
    input("Los datos fueron importados a la base de datos\
         de postgres")     #show message and stop
    os.system('clear')      # clear terminal


def Google():
    #os.system('python export_data_all_phone.py')
    os.system('python google_format_file.py')   
    print ("Archivo disponible en apps/TL_IO/")
    input()
    os.system('clear')
    

def smsmaster ():
    os.system("python export_data_sms.py")
    print ("Archivo sms_master está disponible en apps/TL_IO/")
    input()
    os.system('clear')
    
    
def estadisticas():
    fin = 0
    while (fin==0):
        MostrarMenu()
        opc = int(input("\n\nSelecciones una opción:"))
        if (opc==1):
            Estrellas()
        elif(opc==2):
            Volumen()
        elif(opc==3):
            Cantidad()
        elif(opc==4):
            Ventas()
        elif(opc==6):
            Google()
        elif(opc==5):
            Importar()
        elif(opc==7):
            smsmaster()
        elif(opc==0):
            os.system('clear')
            fin = 1
            
estadisticas()