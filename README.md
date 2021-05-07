# Laboratorio_A01707035
Laboratorio de Github - Emiliano Vásquez Olea

## Acerca del repositorio

Este repositorio fue creado como parte de la evaluación de la Semana Tec *Herramientas computacionales: el arte de la programación*. En el cuál se integran ciertos documentos utilizados para las actividades iniciales de introducción al uso de github como [Programa.c](Programa.c) y [Version.html](Version.html). 

Sin embargo, en la carpeta [Avances Convolución](https://github.com/EmilianoV-TEC/Laboratorio_A01707035/tree/main/Avances%20Convoluci%C3%B3n) se encuentran los scripts que fueron desarrollados a lo largo de la semana en relación con los temas de visión vistos en clase. Estos programas permiten aplicar un filtro a una imagen utilizando convolución.

## Uso del proyecto

### Prerrequisitos

Este proyecto está construido en el lenguaje python, el cuál debe ser descargando desde el siguiente vínculo: [Instalar Python](https://www.python.org/downloads/).

Además, es necesario instalar una serie de librerías para utilizar los scripts, estas son listadas a continuación, junto con el comando para instalarlas utilizando PIP:

* OpenCV
```sh
	pip install opencv-python
```
* Numpy
```sh
	pip install numpy
```
* Matplotlib
```sh
	pip install matplotlib
```
* Argparse
```sh
	pip install argparse
```

### Corrida
Usando la línea de comandos es necesario primero posicionarse en la carpeta de Avances Convolución para correr el script, para ello se puede utilizar el comando cd, un ejemplo sería:
```sh
	cd C:\Users\usr\Proyectos\Laboratorio_A01707035\Avances Convolución
```

Ahora, para correr el programa principal del proyecto es necesario correr el siguiente comando: **python Convolución_ej.py -i [Nombre de la Imagen.jpg]**, reemplazando dicho nombre con la imagen que se encuentre en el mismo folder. Utilizando la imagen de prueba, el comando sería el siguiente:

```sh
	python Convolución_ej.py -i Img_Casa.jpg
```

Al correr el script, este desplegará una serie de imágenes, la original, en blanco y negro, y con el filtro de box blur aplicado. Esta imagen será pasada automáticamente a escala de grises en caso de ser necesario, si esto ocurre se verá un mensaje en la consola indicándolo.

## Referencias y guía de estilo:
* AI Shack(s.f) *Image convolution examples*. Convolutions. Recuperado el 6 de mayo de 2021, de: https://aishack.in/tutorials/image-convolution-examples/

PEP 8

* Rossum G., Warsaw B., Coghlan N. (2001) *PEP 8 -- Style Guide for Python Code*. Python. Recuperado el 6 de mayo de 2021, de: https://www.python.org/dev/peps/pep-0008/