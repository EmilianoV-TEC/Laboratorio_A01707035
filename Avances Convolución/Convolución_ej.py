"""
Programa para realizar la convolución de una matriz, con padding definido y stride de 1
Por Emiliano Vásquez Olea
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
from add_padding import add_padding

def conv_mat(matriz, kernel):
	"""
	Función para realizar convolución sobre una matriz

	Se utiliza la función add_panding para agregar 0s con cierto grosor alrededor de la imagen original
	"""
	matriz = add_padding(matriz, kernel)
	fil_m, col_m = matriz.shape
	fil_k, col_k = kernel.shape
	conv_final = np.zeros(((fil_m-fil_k)+1, (col_m-col_k)+1)) #Se declara matriz con dimensiones finales

	for i in range(conv_final.shape[0]):
		for j in range(conv_final.shape[1]):
			producto = np.multiply(matriz[i:i+fil_k, j:j+col_k], kernel)
			conv_final[i][j] = np.sum(producto)

	return(conv_final)

def filtro_img(imagen, kernel):
	"""
	Función para aplicar filtro y mostrar imagenes
	"""
	plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
	plt.title("Imagen original")
	plt.show()

	if len(imagen.shape) == 3:
		imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
		print("Imagen cambiada a escala de grises")

	plt.imshow(imagen, cmap='gray')
	plt.title("Imagen en escala de grises")
	plt.show()

	imagen_conv = conv_mat(imagen, kernel)

	plt.imshow(imagen_conv, cmap='gray')
	plt.title("Imagen con filtro aplicado")
	plt.show()

	return(imagen_conv)

"""
Se utiliza kernel de ejemplo para probar el código (box blur)
"""
ej_kernel = np.array([[1/9, 1/9, 1/9],
				  [1/9, 1/9, 1/9],
				  [1/9, 1/9, 1/9]])

# Se leen argumentos desde la línea de comandos como "python Convolución_ej.py -i Img_Casa.jpg"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Ruta a imagen")
args = vars(ap.parse_args())
imagen = cv2.imread(args["image"]) 
imagen = filtro_img(imagen, ej_kernel)

