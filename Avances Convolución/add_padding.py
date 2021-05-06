"""
Script para agregar padding a una matriz
Por Emiliano Vásquez Olea
"""
import numpy as np

def add_padding(matriz, kernel):
	"""
	Función para agregar padding a una matriz

	Se calcula una nueva matriz con padding necesario para mantener las dimensiones originales
	"""
	fil_m, col_m = matriz.shape
	fil_k, col_k = kernel.shape
    #Calculamos la cantidad de padding a partir de las dimensiones del kernel
	pad_height = int((fil_k - 1) / 2)
	pad_width = int((col_k - 1) / 2)
	#Creamos matriz con nuevas dimensiones (agregamos padding en los 4 lados)
	matriz_res = np.zeros(((fil_m + pad_height*2), (col_m + pad_width*2)))
	matriz_res[pad_height:fil_m + pad_height, pad_width:col_m + pad_width] = matriz

	return(matriz_res)