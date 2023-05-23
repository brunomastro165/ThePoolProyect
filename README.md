# ThePoolProyect
¡Bienvenidos al proyecto de pool!
![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/9003c84c-9e81-4e4c-b7d7-e8ce11b73b5f)



# Integrantes y tareas

**Bruno Mastropietro**
  Se encargó de la interfaz de usuario, las reglas del juego, la identificación de bochas y turnos, hitboxes de los hoyos, estética visual y unión de código.

**Santiago Rojo**
  Se encargó mayoritariamente de optimizar el código y de correción de errores. Además de la implementación del código general a github y ayudar en la interfaz de usuario.

**Agustin Lobos**
  Se encargó de crear las imagenes y *assets* para el proyecto e importarlas al proyecto, además de su colaboración en las interfaces tanto de usuario como jugables e investigación del lenguaje y entorno. 

**Lucas Nievas**
  Se encargó del sistema de físicas del juego y de su correcta implementación en el programa, además de los sistemas de colisiones entre bochas y ángulos de dirección, además de colaborar en la correción de errores y legibilidad del código.

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
   
   
**Clonar el repositorio**

    git clone https://github.com/brunomastro165/ThePoolProyect.git

**Entrar a la carpeta**
    
    cd ThePoolProyect
    
    python3 main.py
    
**Y listo, está disfrutando de nuestro juego de pool**  

# ADVERTENCIA

Puede suceder que se dé el siguiente error al completar todos los pasos:

![image](https://github.com/brunomastro165/ThePoolProyect/assets/127962081/a5a7dae8-ebaa-45f7-95fe-31e9a9ed69cc)

Esto se debe a una incompatibilidad del sistema de caracteres por defecto de linux, y puede ser solucionado con el siguiente comando:

      sudo apt install unifont
