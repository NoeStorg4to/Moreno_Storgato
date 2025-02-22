# Moreno_Storgato

## Descripción del juego:
Este juego es de la tematica "¿Quién quiere ser millonario?", pero con gatitos. Mientras transcurre el juego se va ganando un monto que se incrementa mientras se conteste correctamente. El premio final (al contrestar 10 preguntas correctamente) es de 1 millon de pesos/dolares. 
El juego inicia con una pagina de inicio en la que luego de hacer click, aparece una imagen por si desea continuar. Al proseguir se le pregunta un nombre al usuario para dejar registrado. Luego empieza el juego con la primer pregunta. El preguntador será un gato elegante, las preguntas son de conocimiento general y se brindan cuatro respuestas posibles para seleccionar. El usuario cuenta con un temporizador de 30 segundos, si se acaba el tiempo pierde el juego, pero si quiere puede continuar volviendo a las preguntas con un click. En el caso de que la respuesta sea incorrecta, el usuario no gana dinero y nuevamente tiene la opcion de volver al juego con un click. En el caso de que conteste bien cada pregunta, se le dará la opción al usuario de proseguir con la siguiente pregunta o retirarse con el dinero asegurado. El premio que haya ganado se guardará en un archivo con el nombre del usuario que haya ingresado al principio. Si contesta todas las preguntas correctamente, finaliza el juego con una felicitación.

## Tabla de Contenidos
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Estructura del juego](#estructura-juego)
## Capturas de Pantalla
![.](las_preguntas.png)
![.](record.png)
![.](eleccion.png)
![.](respuesta_incorrecta.png)
![.](retirarse.png)
![.](final.png)


## Estructura del juego
- main.py: Archivo principal en donde se ejecuta el juego.
- funciones.py: Archivo en donde se cargan todas las funcionalidades del juego y su lógica.
- colores.py: Archivo en donde quedan registrados algunos colores que puedan llegar a utilizarse.
- Imagenes: Carpeta en donde se encuentran todas las imágenes que son utilizadas a lo largo del juego.
- lista_preguntas.json: Archivo json en donde quedan cargadas todas las preguntas con sus respectivas posibles repuestas, y se guarda la respuesta correcta.
- premios.csv: Archivo csv en donde se guardan los premios ganados de cada jugador, con el nombre que halla ingresado el mismo.
