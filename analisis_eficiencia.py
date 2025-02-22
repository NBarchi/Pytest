import time
from itertools import permutations

#Complejidad Exponencial#
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    


#Complejidad Factorial#
def permutaciones(arr):
    return list(permutations(arr))

inicio = time.time()
print(fibonacci(20))
fin = time.time()
print("Tiempo de ejecución:", fin - inicio)

inicio = time.time()
print(permutaciones([1, 2, 3]))
fin = time.time()
print("Tiempo de ejecución:", fin - inicio)