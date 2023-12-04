import random
import time


def busqueda_binaria(lista, objetivo, l_inferior=None, l_superior=None):
    if l_inferior is None:
        l_inferior = 0
    if l_superior is None:
        l_superior = len(lista)-1
    if l_superior < l_inferior:
        return -1
    
    punto_medio = (l_inferior + l_superior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo > lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, punto_medio+1, l_superior)
    else:
        return busqueda_binaria(lista, objetivo, l_inferior, punto_medio-1)
    

if __name__ =='__main__':
    the_black_list = [1, 4, 7, 9, 12]
    print(busqueda_binaria(the_black_list, 12))