import shutil, os
from os import remove	
def deleteHyphen(line):
    line = list(line)
    for i in range(len(line)-1):
        if line[i]== '-':
            line[i] = ''
    return ''.join(line)
f1 = open('/home/argenis/apps/TL_IO/ventas.csv', 'r')
f2 = open('ventas.csv.tmp1', 'w')
for line in f1:
    f2.write(swapDotComa(line))
f1.close()
f2.close()
shutil.copy("ventas.csv.tmp", "/tmp/ventas.csv.tmp")
remove("ventas.csv.tmp1")
remove("ventas.csv.tmp")
