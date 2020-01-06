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
1) Estrellas
2) Volumen
3) Cantidad
4) Ventas

Configuración
-------------
5) Importar datos de venta a base de datos Postgres
6) Crear archivo de contacto formato Google
7) Crear archivo csv para exportar contactos a SmsMaster


0)  Salir
------------""")

def Estrellas():
    sum1 = int(input("Sumando uno:"))
    sum2 = int(input("Sumando dos:"))
    print ("La Suma es:", sum1+sum2)

def Volumen():
       
    #connect to the database
    conn = psycopg2.connect(host='localhost',
                            dbname='todolimpiecito',
                            user='postgres',
                            password='')
    #create a cursor object 
    #cursor object is used to interact with the database
    cur = conn.cursor()
    # Ejecutamos una consulta
    cur.execute("select cliente, suma, dias from volumen order\
                by suma desc fetch first 15 rows only;")
    # Recorremos los resultados y los mostramos
    print('\n\n\n','Total','\t', 'dias','\t','Cliente')
    for cliente, suma, dias in cur.fetchall() :
        print (suma,'\t', dias,'\t',cliente)

    # Cerramos la conexión
    conn.close()
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
    os.system('export_data_all_phone.py')
    os.system('python google_format_file.py')   
    print ("Archivo google_tel_todo.csv disponible en apps/TL_IO/")
    input()
    os.system('clear')
    
def Ventas ():
    try:
        dividendo = int(input("Dividendo:"))
        divisor = int(input("Divisor:"))
        print ("La Division es:", dividendo/divisor)
    except ZeroDivisionError:
        print ("No se Permite la Division Entre 0")

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