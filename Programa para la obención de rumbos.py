print('ESTE PROGRAMA TE AYUDARÁ A CONVERTIR TUS CORDENADAS GEOGRÁFICAS EN RUMBOS')
#Importaremos las librerías necesarisas
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import csv
import math 

#Aqui enlistaras tus columnas
X=[]
Y=[]
V = []
bandera = 0
cantidad = 0

#Abriremos el archivo csv
print('¿Cómo se llama tu archivo?')
nombre = input()
nombre = nombre+ '.csv'

#Aquí leeremos linea por linea del archivo
with open (nombre) as f:
    reader = csv.reader(f)
    print ('Los datos importados son: ')
    print('                           ')
    for row in reader:
        print(row)
    print('                           ')

#Con este código vamos a imprimir por seárado cada columna
with open (nombre) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        X.append(float(row['X']))
        Y.append(float(row['Y']))
        V.append(float(row['V']))
        
while (bandera==0):
    print('¿Cuántos puntos necesitas?')
    cantidad = eval(input())
    h = len(V)
    if (cantidad<=h):
        for i in range(cantidad):
            if i == cantidad-1:
                x2=X[0]
                x1=X[i]
                y2=Y[0]
                y1=Y[i]
            else:
                x2=X[i+1]
                x1=X[i]
                y2=Y[i+1]
                y1=Y[i]

            r = ((x2-x1)/(y2-y1))
            tg = math.atan(r)
            grados = math.degrees(tg)
            
            print('                    ')
            if ((y2-y1)>0) and ((x2-x1)>0):
                print('El rumbo en',V[i],'es',grados,'NE')
            else:
                if ((y2-y1)>0) and ((x2-x1)<0):
                    print('El rumbo en',V[i],'es',grados,'NW')
                else:
                    if ((y2-y1)<0) and ((x2-x1)<0):
                        print('El rumbo en',V[i],'es',grados,'SW')
                    else:
                        print('El rumbo en',V[i],'es',grados,'SE')
                
            bandera = 1
    else:
        print('Me pides más datos de los que tienes registrados, intentalo de nuevo')
        bandera = 0
        
plt.plot(X,Y, Label='Poligono')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plano Catastral')
plt.legend()
plt.show()
