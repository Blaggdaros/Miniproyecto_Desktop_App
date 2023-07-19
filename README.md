# Miniproyecto_Desktop_App

Ejercicio del módulo Aplicaciones de Escritorio del curso Python en Entornos Industriales de la Escuela de Organización Industrial.

Más concretamente:

## Miniproyecto - Aplicaciones de escritorio

### Introducción

La tarea consiste en crear una pequeña aplicación de escritorio que combina las ideas que
vimos en clase, junto con unos pocos elementos nuevos pero que continúan con la filosofía
de widgets con las que estamos familiarizados. La aplicación se trata de un editor de
Markdown compuesto de dos secciones principales: un editor de textos en la zona izquierda
y un navegador web embebido en la zona derecha. El uso normal de la aplicación consiste
en escribir Markdown en el editor de la izquierda, pulsar el botón etiquetado como "Render
markdown" y obtener una vista renderizada del código Markdown a la derecha en formato
HTML.

### Descripción

La edición de texto se hará sobre un QPlainTextEdit , que ya incorpora las
funcionalidades estándar de un bloque de entrada de texto tales como copiar/pegar,
selección con el ratón, movimiento del cursor usando las teclas de dirección, etc. Por otro
lado, la representación del texto renderizado se hará sobre un widget tipo
QWebEngineView , que incorpora un motor de renderizado web completo y comparte
muchas características con navegadores web habituales como Google Chrome y Firefox,
como por ejemplo cargar una URL.

La organización de los widgets será con un layout anidado tal y como vimos en clase: un
QHBoxLayout principal que tiene un QVBoxLayout a la izquierda y un
QWebEngineView a la derecha. El QVBoxLayout , a su vez, agrupa el
QPlainTextEdit arriba y un QPushButton abajo. Una vez se hace click en este
botón, el contenido actual del QPlainTextEdit se convierte a HTML utilizando alguna
librería disponible a tal efecto (más información a continuación) y se le pasa el HTML
generado al QWebEngineView de la derecha para su visualización.

### Consejos

- QWebEngineView es una clase definida en el paquete QtWebEngineWidgets , el
cual no viene en la instalación por defecto de PyQt6. Es necesario instalarlo aparte
ejecutando pip install PyQt6-WebEngine dentro del virtualenv.
- También es posible que sea necesario instalar algunas librerías extras a nivel del
sistema operativo (en la consola de WSL): sudo apt install libnss3 libxdamage1 libasound2.
- Una vez instalado, la manera correcta de importar QWebEngineView en el código es
from PyQt6.QtWebEngineWidgets import QWebEngineView.
- Para generar el HTML correspondiente a un Markdown dado, se pueden utilizar varias
librerías ya existentes para ello; por ejemplo, pandoc o python-markdown2.
- Como es habitual, se recomienda leer bien la documentación de las clases de Qt
implicadas, en especial los métodos públicos y los signals/slots. Por ejemplo, para
indicarle al QWebEngineView el contenido HTML a mostrar se puede utilizar el
método setHtml().

### Mejoras opcionales

Si se observa cuidadosamente la captura de pantalla anterior, se puede ver una barra de
menú en la parte superior, constando de dos items: File y Help.

#### Con respecto a File

Se sugiere implementar algunas de las funcionalidades
estándar tales como nuevo, abrir, guardar y cerrar. Abrir se refiere a un fichero
Markdown previamente presente en el sistema de ficheros, y guardar se refiere a volcar
el contenido actual del QPlainTextEdit en un fichero nuevo (o sobreescribir uno
existente).

#### Con respecto a Help

Se sugiere mostrar un submenú con una única acción
etiquetada "Acerca de". Al hacer click en ella, se puede mostrar un diálogo breve con una
pequeña descripción del programa y/o una mención al autor.

Para implementar estas funcionalidades será necesario investigar algunos componentes
nuevos que no llegamos a ver en las clases, como por ejemplo QFileDialog y
QMessageBox. Se recomienda estudiar el capítulo 4 del libro Python and Qt: The Best
Parts, que se puede leer online [aquí](https://drive.google.com/file/d/1PK2yP-QX7fzxxVIeOib6e0TE5WH8X6Am/view) (22 páginas).
