# ThePoolProyect
**¡Bienvenidos al proyecto de pool!**


![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/9003c84c-9e81-4e4c-b7d7-e8ce11b73b5f)


# Breve descripción del proyecto

La idea del proyecto que estamos realizando es la de un juego clásico de Pool, al cual hemos querido darle una estética minimalista y un funcionamiento realista, principalmente en las reglas y condiciones de victoria del mismo. 

Para llevar a cabo el proyecto que tenemos entre manos, hemos utilizado el lenguaje Python junto con las librerías Pygame y Pymunk.

El mismo tiene incorporadas ya todas las reglas básicas del juego, las físicas, las colisiones, sistema turnos y un modo de juego contra un bot con 3 dificultades, además de una estética visual sencilla y agradable, una interfaz de usuario bonita y amigable para la vista y una amplia variedad música para acompañar a la experiencia del juego.


# Integrantes y tareas

**Bruno Mastropietro**
  Se encargó crear la interfaz de usuario, las reglas del juego, el palo y su ángulo, la identificación de bochas y turnos, hitboxes de los hoyos y su respectiva función, estética visual, música y unión de código.

**Santiago Rojo**
  Se encargó mayoritariamente de optimizar el código y de correción de errores. Además de la implementación del código general a github, ayudar en la interfaz de usuario y creación del bot y niveles de dificultad.

**Agustin Lobos**
  Se encargó de crear las imagenes y *assets* para el proyecto e importarlas al mismo, además de su colaboración en las interfaces tanto de usuario como jugables, colaboró en la creación del bot y realizó investigación del lenguaje y entorno. 

**Lucas Nievas**
  Se encargó del sistema de físicas del juego y de su correcta implementación en el programa, además de los sistemas de colisiones entre bochas y ángulos de dirección, colaboracion en la correción de errores y legibilidad del código, e implementación de música.

  **Tareas conjuntas**
  La mayoría del código fué realizado mediante la función *code with me* que proveen los IDE´s de JetBrains, por lo que la gran mayoría de código fué realizado entre todos en reuniones diarias,
  mayoritariamente se hicieron commits desde las pcs con las que se podía usar linux para corroborar su funcionamiento. 


# Iniciar el proyecto desde 0
Para iniciar el proyecto desde 0, vamos a seguir la siguiente lista de pasos:

**Instalación de git**

    sudo apt install git
   
**Comprobación**
    
    git --version
    
**Instalación de Python y sus dependencias**

Python, por defecto, viene instalado en las distribuciones linux más utilizadas, sin embargo, de ser necesaria su instalación, haremos lo siguiente:

    sudo apt install python3
    
**Comprobación**

    python3 --version
    
    
**Instalación de pip**
    
    sudo apt update
    
    sudo apt install curl
    
    wget https://bootstrap.pypa.io/get-pip.py
    
    sudo apt install python3-pip
    
    pip install pip==22.3.1 --break-system-packages
    
**Instalación de las librerías pygame y pymunk**
   
    pip install pygame
    
    pip install pymunk
   
   
**Corrección de un error importante**
    Correción de error de compatibilidad con diferentes tipos de pantallas y sistemas:
    
    sudo apt install unifont
    
**Clonar el repositorio**

    git clone https://github.com/brunomastro165/ThePoolProyect.git

**Entrar a la carpeta**
    
    cd ThePoolProyect
    
    python3 main.py
    
**Y listo, está disfrutando de nuestro juego de pool**  

# Avances en el proyecto

![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/90e8aacb-ec12-48e5-8f3b-de3431808671)
![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/c91b75f1-e078-4cd0-a354-819e1c8863c9)
![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/565341cd-7608-40b3-9519-15bbee2000d7)
![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/dac813f2-c5c6-4a55-8e37-469e78e297de)
![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/37279b95-a052-49f2-b966-144f3128fd63)
![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/e706e518-4149-4e73-a299-0f799fb64f32)
![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/700230f7-83b2-46d9-b0be-a803039dd608)
![11-24-28](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/5a9456f2-898f-4c21-89ad-ce4c0d6dc210)





# ADVERTENCIAS

**Error con el sistema de caracteres de un sistema operativo**
Puede suceder que se dé el siguiente error al completar todos los pasos:

![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/a5a7dae8-ebaa-45f7-95fe-31e9a9ed69cc)

Esto se debe a una incompatibilidad del sistema de caracteres por defecto de linux, y puede ser solucionado con el siguiente comando:

      sudo apt install unifont
     
**Pantalla negra al iniciar el juego**

Si llega a suceder que hay una pantalla negra al momento de iniciar el juego, recomendamos simplemente mover la ventana del juego con el mouse, esto soluciona el problema (solo se da en situaciones demasiado específicas)
