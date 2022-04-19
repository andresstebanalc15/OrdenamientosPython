import random
import time
import numpy as np
from matplotlib import pyplot as plt

randomlist = []
tiempo1 = []
tiempo2 = []
def burbuja_tradicional(arreglo):
    global tiempo 

    # Calculamos la longitud del arreglo para tener un código más limpio
    longitud = len(arreglo)
    # Recorremos todo el arreglo
    inicio = time.time()
    for i in range(longitud):
        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            # Si el actual es mayor que el siguiente, ...
            # Nota: para un orden inverso, cambia `>` por `<`
             
            if arreglo[indice_actual] > arreglo[indice_siguiente_elemento]:
                # ... intercambiamos los elementos
                arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]
        fin = time.time()
        tiempo1.append(fin-inicio)

def burbujamejorado(l):
    global tiempo2 
    inicio = time.time()

    for pasada in range(1, len(l)-1):
        for i in range(0,len(l)-pasada):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
        fin = time.time()
        tiempo2.append(fin-inicio)
    return l

print("Introduzca la cantidad de datos aleatorios a comparar")
datos = input()
datos = int(datos)

for i in range(0,datos):
    n = random.randint(1,datos)
    randomlist.append(n)
  
burbuja_tradicional(randomlist)
burbujamejorado(randomlist)

x = np.arange(0, len(tiempo1))
x2 = np.arange(0, len(tiempo2))

y = tiempo1
y2 = tiempo2
plt.title("Burbuja tradicional vs burbuja mejorada")
plt.xlabel("Cantidad de datos")
plt.ylabel("Tiempo en segundos")
plt.plot(x, y,color="blue", linewidth=2.5, linestyle="-", label="Burbuja tradicional")

plt.plot(x2, y2,color="red", linewidth=2.5, linestyle="-", label="Burbuja mejorada")
plt.legend(loc='upper left')

plt.show()