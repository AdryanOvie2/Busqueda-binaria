import random
import time

def busqueda_binaria(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

the_black_list = [1, 4, 7, 9, 12]

num = 9

if busqueda_binaria(the_black_list, num) > 0:
    print(f"\nEl valor {num} se encuentra en la lista\n")
else:
    print(f"\nEl valor {num} no se encuentra en la lista\n")

