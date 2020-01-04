import shutil, os
from os import remove	
def swapDotComa(line):
    """ Search for a coma inside doble quoted words and change it to dot.
    this may be used to change LATIN , used in decimal for . used in
    American notation."""


    # We start outside a doble quote
    quoted = False
    line = list(line)
    for i in range(len(line)-1):
        if line[i]== '"':
            quoted = not quoted
        elif quoted and line[i]==',':
            line[i] = '.'
        elif quoted and line[i]=='.':
            line[i] = ','
    return ''.join(line)

def deleteDobleQuoted(line):
    """ Search for a doble quoted words and change it to nothing.
    this may be used to change LATIN , used in decimal for . used in
    American notation."""
    
    line = list(line)
    for i in range(len(line)-1):
        if line[i]== '"':
            line[i] = ''
    return ''.join(line)


f1 = open('/home/argenis/apps/TL_IO/ventas.csv', 'r')
f2 = open('ventas.csv.tmp1', 'w')
f3 = open('ventas.csv.tmp', 'w')
for line in f1:
    f2.write(swapDotComa(line))
f2.close()
f2 = open('ventas.csv.tmp1', 'r')
for line in f2:
    f3.write(deleteDobleQuoted(line))
f1.close()
f2.close()
f3.close()

shutil.copy("ventas.csv.tmp", "/tmp/ventas.csv.tmp")
remove("ventas.csv.tmp1")
remove("ventas.csv.tmp")
