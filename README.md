### Hola,

Este es un pequeño proyecto donde pongo en muestra mis habilidades y conocimientos sobre el manejo de Selenium WeDriver para el testing automatizado.

El sitio web que al que se hace testing lo conocí de un curso dado por "Let's Kode It". El cual este pequeño proyecto consiste en tres casos de prueba.


# Sobre el proyecto

####Caso 1
Los primeros dos casos son para hacer test al sistema de logeo. Al no crear una cuenta, simplemente nos enfocamos en ingresar texto y localizar los botones.

####Caso 2
El ultimo caso de prueba consiste en ingresar al sitio y nos enfocamos en la búsqueda de uno o varios cursos (depende del archivo "test" que se ejecute). Después de encontrar el curso simulara una compra inconclusa y se tratará de localizar algún mensaje de error.

Instrucciones
-------------
####Paso 1

En la dirección "/base/webdriverfactory.py" debemos agregar la dirección donde se encuentre el driver.

####Paso 2
Si queremos ejecutar únicamente el archivo "/test/courses/courses_using_cvs_test.py" debemos ejecutar el siguiente comando, dentro de la carpeta del proyecto:

	"py.test -s -v test/courses/courses_using_cvs_test.py"

####Paso 3
Para ejecutar el programa:

- Asegurarse de que la dirección del driver fue completado.
- En la terminal estar dentro de la carpeta del proyecto y ejecutar el siguiente comando:

		"py.test test/test_suite_demo.py"


Gracias al curso de "Let's Kode It". Obtuve las enseñanzas de un mejor manejo de Selenium WebDriver con buenas prácticas. Gracias a este curso tome las bases para construir este proyecto.
