import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1): #Orden de complejidad: O(n)
        result *= i
    return result

def factorial_recursive(n):
    if n == 1 or n == 0: return 1
    return n * factorial_recursive(n - 1)  #Orden de complejidad: O(n)



num = int(input("Ingresa un número entero fi: "))
inicio = time.time() #Orden de complejidad: O(1)
print("El factorial de", num, "es", factorial_iterative(num)) #Orden de complejidad: O(n)
fin = time.time() #Orden de complejidad: O(1)
print("Tiempo de ejecución iterativo:", fin - inicio)

num1 = int(input("Ingresa un número entero fr: "))
inicio1 = time.time()
print("El factorial de", num1, "es", factorial_recursive(num1))
fin1 = time.time()
print("Tiempo de ejecución recursivo:", fin1 - inicio1)


