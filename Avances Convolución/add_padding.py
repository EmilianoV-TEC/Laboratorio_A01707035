"""
Función para agregar padding a una matriz
Por Emiliano Vásquez Olea
"""
import numpy as np

def add_padding(matriz, padding):
    fil_m, col_m = matriz.shape
    #Creamos matriz con nuevas dimensiones (agregamos padding en los 4 lados)
    matriz_res = np.zeros(((fil_m+padding*2), (col_m+padding*2)))
    matriz_res[padding:fil_m+padding, padding:col_m+padding] = matriz

    return(matriz_res)