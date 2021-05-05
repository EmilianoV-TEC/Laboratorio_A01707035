"""
Programa para realizar la convolución de una matriz, sin padding y stride de 1
"""

import cv2
import numpy as np

def conv_mat(matriz, kernel):
	fil_m, col_m = matriz.shape
	fil_k, col_k = kernel.shape
	conv_final = np.zeros(((fil_m-fil_k)+1, (col_m-col_k)+1)) #Se declara matriz con dimensiones finales
	for i in range(conv_final.shape[0]):
		for j in range(conv_final.shape[1]):
			producto = np.multiply(matriz[i:i+fil_k, j:j+col_k], kernel)
			conv_final[i][j] = np.sum(producto)

	return(conv_final)


"""
Se utilizan matrices de ejemplo para probar el código
"""
ej_matriz = np.array([[10, 4, 50, 30, 20], 
				 	  [80, 0, 0, 0, 6],
				 	  [0, 0, 1, 16, 17],
				 	  [0, 1, 0, 7, 23],
				 	  [1, 0, 6, 0, 4]])

ej_kernel = np.array([[1, 0, 1],
					  [0, 0, 0],
					  [1, 0, 3]])

final = conv_mat(ej_matriz, ej_kernel)
print(final)
