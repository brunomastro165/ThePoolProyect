# Informe de Nuestro Proyecto 

## Fase de Planificación  y Definición 

Al comenzar tuvimos que decidir que lenguaje utilizar para poder programar el proyecto aún por determinar. Decidimos usar Python, ya que sabíamos que era un lenguaje de programación que permite realizar una amplia variedad de programas.
 
Después de saber qué lenguaje de programación utilizar, investigamos las posibilidades que tenía y encontramos muchas librerías para desarrollar software y entre ellas encontramos Pygame, una librería para hacer videojuegos que nos proporciona varias funciones con las que trabajar. 

Luego decidimos que tipo de juego íbamos a hacer, considerando las opciones que teníamos en la plataforma dadas por el profesor y algunas que nos iban surgiendo. Al final nos decantamos por hacer un juego de pool. 

## Inicio del desarrollo 

La primera parte del desarrollo consistió en investigar el lenguaje de Python junto con Pygame, ya que no teníamos conocimiento previo de ninguno de estos apartados. A medida que aprendíamos sobre estas partes íbamos haciendo pequeñas cosas en el desarrollo. Entre esas cosas se encuentra la creación del diseño conceptual de las imágenes a utilizar y también el diseño del menú y la interfaz de usuario. También investigamos algunos proyectos similares para poder usar de referencia, en lo que  más nos enfocamos fue:
- Métodos para hacer las físicas del juego
- Cargar imágenes y que estuviesen en movimiento
- Creación de objetos en Python  
- Desarrollo de videojuegos en general. 

Después de mucha investigación nos topamos con la librería de PyMunk que es una librería hecha para crear físicas realistas creando cuerpos y que se integra con PyGame. A partir de este punto decidimos dividirnos en dos equipos, uno de estos equipos continuo realizando el menú y la interfaz utilizando PyGame y decidiendo como se va a implementar con PyMunk y el otro equipo realiza la investigación de esta última librería para poder usarla y generar las mecánicas básicas del juego de pool para posteriormente implementarlo y que este equipo enseñe al otro como funciona, además este último equipo realizo el material básico para la representación visual de la mesa y las bolas de pool. 

## Mecánicas y Partes Avanzadas 

Al llevar a cabo cada parte por separado, unimos los dos códigos e hicimos que desde el menú se active el juego de pool, este solo contaba con las mecánicas básicas de tirar la bola blanca, meter bolas, colisiones entre bolas y colisiones con las partes de la mesa. Al llevar a cabo esta implantación nos decidimos a terminar con las partes más esenciales del menú del juego, las cuales fueron, hacer un apartado de opciones para modificar el sonido, la pantalla en el juego y la dificultad. 

Después de esto procedimos a programar más reglas para el juego, entre ellas, el sistema de turnos de cada jugador, el sistema para detectar que tipo de bolas de meter cada jugador y cuando meta la bola negra el jugador del turno actual pierde, este apartado todavía está en proceso. En paralelo estamos desarrollando el modo de juego contra un bot que tendrá distintas dificultades y que también está aún en desarrollo 
