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
6) Cambiar comas por puntos
7) Crear archivo de contacto formato Google
8) Crear archivo cvs para Sms Master


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
    cur.execute("select cliente from ventas_la_carlota group by cliente order by cliente asc;")
    # Recorremos los resultados y los mostramos
    for cliente in cur.fetchall() :
        print (cliente)

    # Cerramos la conexión
    conn.close()
    input()
    os.system('clear')

def Importar():
#connect to the database
    conn = psycopg2.connect(host='localhost',
                            dbname='todolimpiecito',
                            user='postgres',
                            password='')
    #create a cursor object 
    #cursor object is used to interact with the database
    cur = conn.cursor()
    # Ejecutamos una consulta
    cur.execute("\copy ventas_la_carlota (Fecha,CodCli,Cliente,Telefono,Cantidad,Descripción,Precio,Locación,Semana) from '/tmp/ventas.csv.tmp' delimiter ',' csv header;")
    commit()
    # Cerramos la conexión
    conn.close()
    input()
    os.system('clear')


def Google():

    f1 = open('/tmp/tel_todo.csv', 'r')
    f2 = open('/home/argenis/apps/TL_IO/google_tel_todo.csv', 'w')
    entrada = csv.DictReader(f1)
    f2.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value'+'\n')
    for reg in entrada:
        f2.write('11AA '+reg['cliente']+',,,,,,,,,,,,,,,,,,,,,,,,,Avenida B,,,* Avenida B ::: * Avenida B,Mobile,'+reg['telefono']+'\n')
    f1.close()
    f2.close()
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
        elif(opc==5):
            Importar()
        elif(opc==7):
            Google()
        elif(opc==0):
            os.system('clear')
            fin = 1
            
estadisticas()