import random
import time
import numpy as np
from matplotlib import pyplot as plt

randomlist = []
tiempo1 = []
tiempo2 = []
def insercion(A):
    global tiempo 
    inicio = time.time()
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j];
                A[j]=A[j-1];
                A[j-1]=aux;
        fin = time.time()
        tiempo1.append(fin-inicio)

def seleccion(A):
    global tiempo2 
    inicio = time.time()

    for i in range(len(A)):
        minimo=i;
        for j in range(i,len(A)):
            if(A[j] < A[minimo]):
                minimo=j;
        if(minimo != i):
            aux=A[i];
            A[i]=A[minimo];
            A[minimo]=aux;
        fin = time.time()
        tiempo2.append(fin-inicio)
   

print("Introduzca la cantidad de datos aleatorios a comparar")
datos = input()
datos = int(datos)

for i in range(0,datos):
    n = random.randint(1,datos)
    randomlist.append(n)
  
insercion(randomlist)
seleccion(randomlist)

x = np.arange(0, len(tiempo1))
x2 = np.arange(0, len(tiempo2))

y = tiempo1
y2 = tiempo2
plt.title("Selección vs inserción")
plt.xlabel("Cantidad de datos")
plt.ylabel("Tiempo en segundos")
plt.plot(x, y,color="blue", linewidth=2.5, linestyle="-", label="Inserción")
plt.plot(x2, y2,color="red", linewidth=2.5, linestyle="-", label="Selección")
plt.legend(loc='upper left')

plt.show()