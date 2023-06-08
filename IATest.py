import math
import time

#import numpy
import cmath
import pygame

def area_triangulo(a,b,c):
    semi_perimetro = (a + b + c) / 2
    return math.sqrt(semi_perimetro*(semi_perimetro-a)*(semi_perimetro-b)*(semi_perimetro-c))
def calcular_lado(ab,ac,angulo):
    r_angulo = math.radians(angulo)
    # calcula el lado opuesto del angulo junto con los lados que conforman el angulo
    return math.sqrt(ab**2 + ac**2 - (2*ab*ac) * math.cos(r_angulo))
def sacar_angulo(a, b, c):
    cos_value = 0
    # "a" es el lado opuesto al angulo
    if (a**2-b**2-c**2) != 0:
        cos_value = -((a**2-b**2-c**2)/(2*b*c))
        if -1 < cos_value < 1:
            return math.acos(cos_value) * (180 / math.pi)
        else:
            return 0
    else:
        return 90

def se_puede(blancaX,blancaY,bolaX,bolaY,hoyoX,hoyoY,diam):
    # lado1: de la blanca a la bola a embocar
    lado1 = sacar_hipotenusa_puntos(blancaX, blancaY, bolaX, bolaY)
    # lado2: de la blanca al hoyo
    lado2 = sacar_hipotenusa_puntos(blancaX, blancaY, hoyoX, hoyoY)
    # lado3: de la bola a embocar al hoyo
    lado3 = sacar_hipotenusa_puntos(hoyoX, hoyoY, bolaX, bolaY)

    nuevoLado3 = lado3 + diam
    if sacar_angulo(lado2, lado1, nuevoLado3) < 90:
        return False
    else:
        return True

def sacar_hipotenusa_puntos(x1,y1,x2,y2):
    if x1 > x2:
        x = x1 - x2
    else:
        x = x2 - x1

    if y1 > y2:
        y = y1 - y2
    else:
        y = y2 - y1



    hipotenusa = math.sqrt((x**2) + (y**2))
    return hipotenusa
"""
def sacar_verticeY(d, c, a, b, h, j ):
    if b == j and a - h != 0:
        return 1/2*(2*j - 2 * math.sqrt((((a**2-c**2+d**2-h**2)**2)/4*(a-h)**2+((h*(a**2-c**2+d**2-h**2))/(a-h))+(d**2-h**2))))
    elif a == h - cmath.sqrt(-(b-j)**2) and cmath.sqrt(-(b-j)**2)*(-(c**2-d**2)) != 0:
        return (-4*b**2*d**2+4*b*d**2*j-c**4+2*c**2*d**2-4*c**2*j**2-d**4)/4*(b-j)*(c**2-d**2)
    elif a == cmath.sqrt(-(b-j)**2)+h and cmath.sqrt(-(b-j)**2)*(c**2-d**2) != 0:
        return (-4*b**2*d**2+4*b*d**2*j-c**4+2*c**2*d**2-4*c**2*j**2-d**4)/4*(b-j)*(c**2-d**2)
    elif a**2-2*a*h+b**2-2*b*j+h**2+j**2 != 0 and b-j != 0:
        return (a**2* b**2 - a**2 *j**2 + a* math.sqrt(-(b - j)**2 *(a**4 - 4* a**3 *h + 2* a**2* b**2 - 4* a**2* b* j
        - 2* a**2* c**2 - 2* a**2* d**2 + 6 *a**2* h**2 +2* a**2* j**2 - 4* a* b**2* h + 8* a* b* h* j + 4*
        a* c**2* h + 4* a* d**2* h - 4* a* h**3 - 4* a* h*j**2 + b**4 - 4* b**3* j - 2* b**2* c**2 - 2* b**2*
        d**2 + 2 *b**2* h**2 + 6* b**2* j**2 + 4* b* c**2* j + 4* b* d**2* j - 4* b* h**2* j - 4* b* j**3 +
        c**4 - 2* c**2* d**2 - 2* c**2* h**2 - 2* c**2*j**2 + d**4 - 2* d**2* h**2 - 2* d**2* j**2 + h**4
        + 2* h**2* j**2 + j**4)) - h* math.sqrt(-(b - j)**2
        *(a**4 - 4 *a**3* h + 2* a**2* b**2 - 4* a**2* b* j - 2* a**2* c**2 - 2* a**2* d**2 + 6* a**2* h**2 + 2* a**2*
          j**2 - 4* a* b**2* h + 8* a* b* h* j + 4* a* c**2* h + 4* a* d**2* h - 4* a* h**3 - 4* a* h* j**2 + b**4 - 4*
          b**3* j - 2* b**2* c**2 - 2* b**2* d**2 + 2* b**2* h**2 + 6* b**2* j**2 + 4* b* c**2* j + 4* b* d**2* j - 4*
          b* h**2* j - 4* b* j**3 + c**4 - 2* c**2* d**2 - 2* c**2* h**2 - 2* c**2* j**2 + d**4 - 2* d**2* h**2 - 2*
          d**2* j**2 + h**4 + 2* h**2* j**2 + j**4)) - 2* a* b**2* h + 2* a* h* j**2 + b**4 - 2* b**3* j - b**2* c**2 +
                b**2* d**2 + b**2* h**2 + 2* b* c**2* j - 2* b* d**2* j + 2* b* j**3 - c**2* j**2 + d**2* j**2 - h**2*
                j**2 - j**4)/(2* (b - j)* (a**2 - 2* a* h + b**2 - 2* b* j + h**2 + j**2))
    elif a**2 - 2*a*h+b**2-2*b*j+h**2+j**2 != 0 and b- j != 0:
        return (a ** 2* b ** 2 - a ** 2* j ** 2 - a* math.sqrt(-(b - j) ** 2*(a ** 4 - 4*
        a ** 3*
        h + 2*
        a ** 2*
        b ** 2 - 4*
        a ** 2*
        b*
        j - 2*
        a ** 2*
        c ** 2 - 2*
        a ** 2*
        d ** 2 + 6*
        a ** 2*
        h ** 2 + 2*
        a ** 2*
        j ** 2 - 4*
        a*
        b ** 2*
        h + 8*
        a*
        b*
        h*
        j + 4*
        a*
        c ** 2*
        h + 4*
        a*
        d ** 2*
        h - 4*
        a*
        h ** 3 - 4*
        a*
        h*
        j ** 2 + b ** 4 - 4*
        b ** 3*
        j - 2*
        b ** 2*
        c ** 2 - 2*
        b ** 2*
        d ** 2 + 2*
        b ** 2*
        h ** 2 + 6*
        b ** 2*
        j ** 2 + 4*
        b*
        c ** 2*
        j + 4*
        b*
        d ** 2*
        j - 4*
        b*
        h ** 2*
        j - 4*
        b*
        j ** 3 + c ** 4 - 2*
        c ** 2*
        d ** 2 - 2*
        c ** 2*
        h ** 2 - 2*
        c ** 2*
        j ** 2 + d ** 4 - 2*
        d ** 2*
        h ** 2 - 2*
        d ** 2*
        j ** 2 + h ** 4 + 2*
        h ** 2*
        j ** 2 + j ** 4)) + h*
        math.sqrt(-(b - j) ** 2*(a ** 4 - 4*
        a ** 3*
        h + 2*
        a ** 2*
        b ** 2 - 4*
        a ** 2*
        b*
        j - 2*
        a ** 2*
        c ** 2 - 2*
        a ** 2*
        d ** 2 + 6*
        a ** 2*
        h ** 2 + 2*
        a ** 2*
        j ** 2 - 4*
        a*
        b ** 2*
        h + 8*
        a*
        b*
        h*
        j + 4*
        a*
        c ** 2*
        h + 4*
        a*
        d ** 2*
        h - 4*
        a*
        h ** 3 - 4*
        a*
        h*
        j ** 2 + b ** 4 - 4*
        b ** 3*
        j - 2*
        b ** 2*
        c ** 2 - 2*
        b ** 2*
        d ** 2 + 2*
        b ** 2*
        h ** 2 + 6*
        b ** 2*
        j ** 2 + 4*
        b*
        c ** 2*
        j + 4*
        b*
        d ** 2*
        j - 4*
        b*
        h ** 2*
        j - 4*
        b*
        j ** 3 + c ** 4 - 2*
        c ** 2*
        d ** 2 - 2*
        c ** 2*
        h ** 2 - 2*
        c ** 2*
        j ** 2 + d ** 4 - 2*
        d ** 2*
        h ** 2 - 2*
        d ** 2*
        j ** 2 + h ** 4 + 2*
        h ** 2*
        j ** 2 + j ** 4)) - 2*
        a*
        b ** 2*
        h + 2*
        a*
        h*
        j ** 2 + b ** 4 - 2*
        b ** 3*
        j - b ** 2*
        c ** 2 + b ** 2*
        d ** 2 + b ** 2*
        h ** 2 + 2*
        b*
        c ** 2*
        j - 2*
        b*
        d ** 2*
        j + 2*
        b*
        j ** 3 - c ** 2*
        j ** 2 + d ** 2*
        j ** 2 - h ** 2*
        j ** 2 - j ** 4) / (2*(b - j)(a ** 2 - 2* a* h + b ** 2 - 2* b* j + h ** 2 + j ** 2))
    else:
        print("hola")
        return 1
        """
"""
def sacar_verticeX(d, c, a, b, h, j ):
    if b == j and a - h != 0:
        return (a**2-c**2+d**2-h**2)/(2*(a-h))
    elif a == h - cmath.sqrt(-(b - j) ** 2) and math.sqrt(-(b - j) ** 2) * (-(c ** 2 - d ** 2)) != 0:
        return (-4*b**2*d**2+4*c**2*h*math.sqrt(-(b-j)**2)-4*d**2*h*math.sqrt(-(b-j)**2)+8*b*d**2*j+c**4-2*c**2*d**2+d**4-4*d**2*j**2)/(4*math.sqrt(-(d-j)**2)*(c**2-d**2))
    elif a == cmath.sqrt(-(b-j)**2)+h and cmath.sqrt(-(b-j)**2)*(c**2-d**2) != 0:
        return (-4*b**2*d**2+4*c**2*h*math.sqrt(-(b-j)**2)-4*d**2*h*math.sqrt(-(b-j)**2)+8*b*d**2*j-c**4+2*c**2*d**2-d**4+4*d**2*j**2)/(4*math.sqrt(-(d-j)**2)*(c**2-d**2))
    elif a**2-2*a*h+b**2-2*b*j+h**2+j**2 != 0 and b-j != 0:
        return (a ** 3 - a ** 2* h - math.sqrt(-(b - j) ** 2*(a ** 4 - 4*
        a ** 3*h + 2*a ** 2*b ** 2 - 4*a ** 2*b*j - 2*a ** 2*c ** 2 - 2*a ** 2*d ** 2 + 6*a ** 2*h ** 2 + 2*a ** 2*
        j ** 2 - 4*a*b ** 2*h + 8*a*b*h*j + 4*a*c ** 2*h + 4*a*d ** 2*h - 4*a*h ** 3 - 4*a*h*j ** 2 + b ** 4 - 4*b ** 3*
        j - 2*b ** 2*c ** 2 - 2*b ** 2*d ** 2 + 2*b ** 2*h ** 2 + 6*b ** 2*j ** 2 + 4*b*c ** 2*j + 4*b*d ** 2*
        j - 4*b*h ** 2*j - 4*b*j ** 3 + c ** 4 - 2*c ** 2*d ** 2 - 2*c ** 2*h ** 2 - 2*c ** 2*j ** 2 + d ** 4 - 2*
        d ** 2*h ** 2 - 2*d ** 2*j ** 2 + h ** 4 + 2*h ** 2*j ** 2 + j ** 4)) + a*b ** 2 - 2*a*b*j - a*c ** 2 + a*
        d ** 2 - a*h ** 2 + a*j ** 2 + b ** 2*h - 2*b*h*j + c ** 2*h - d ** 2*h + h ** 3 + h*
        j ** 2) / (2*(a ** 2 - 2 *a* h + b ** 2 - 2* b* j + h ** 2 + j ** 2))
    elif a**2 - 2*a*h+b**2-2*b*j+h**2+j**2 != 0 and b- j != 0:
        return (a**3 - a**2** h + math.sqrt(-(b - j)**2* (a**4 - 4* a**3* h + 2* a**2* b**2 - 4* a**2* b* j - 2* a**2*
        c**2 - 2* a**2* d**2 + 6* a**2* h**2 + 2* a**2* j**2 - 4* a* b**2* h + 8* a* b* h* j + 4* a* c**2* h + 4* a*
        d**2* h - 4* a* h**3 - 4* a* h* j**2 + b**4 - 4* b**3 * j - 2* b**2* c**2 - 2* b**2* d**2 + 2* b**2* h**2 + 6*
        b**2* j**2 + 4* b* c**2* j + 4* b* d**2* j - 4* b* h**2* j - 4* b* j**3 + c**4 - 2* c**2* d**2 - 2* c**2* h**2
        - 2* c**2* j**2 + d**4 - 2* d**2* h**2 - 2* d**2* j**2 + h**4 + 2* h**2 *j**2 + j**4)) + a* b**2 - 2* a* b* j
        - a* c**2 + a* d**2 - a* h**2 + a* j**2 + b**2* h - 2* b* h* j + c**2* h - d**2* h + h**3 + h* j**2)/(2* (a**2
        - 2* a* h + b**2 - 2* b* j + h**2 + j**2))
    else:
        print("hola")
        return 1
"""
def triangulo_de_tirada(blancaX,blancaY,bolaX,bolaY,hoyoX,hoyoY,diam,window):

    # lado1 se usa para sacar el angulo opuesto

    # lado1: de la blanca a la bola a embocar
    lado1 = sacar_hipotenusa_puntos(blancaX, blancaY, bolaX, bolaY)
    # lado2: de la blanca al hoyo
    lado2 = sacar_hipotenusa_puntos(blancaX, blancaY, hoyoX, hoyoY)


    # lado3: de la bola a embocar al hoyo
    lado3 = sacar_hipotenusa_puntos(hoyoX, hoyoY, bolaX, bolaY)
    """
    pygame.draw.line(window, (255, 0, 0), (blancaX, blancaY), (bolaX, bolaY))
    pygame.draw.line(window, (255, 0, 0), (bolaX, bolaY), (hoyoX, hoyoY))
    pygame.draw.line(window, (255, 0, 0), (blancaX, blancaY), (hoyoX, hoyoY))
    """

    if sacar_angulo(lado3,lado2,lado1) < 1:
        if bolaX < blancaX:
            x = blancaX - bolaX
        else:
            x = bolaX -blancaX
        if bolaY < blancaY:
            y = blancaY - bolaY
        else:
            y = bolaY - blancaY
        angulo = sacar_angulo(y, x, lado1)
    else:
        # angulo del vertice del hoyo
        angulo_opuesto = sacar_angulo(lado1, lado2, lado3)


        nuevoLado3 = lado3 + diam-6
        nuevoLado1 = calcular_lado(lado2, nuevoLado3, angulo_opuesto)


        angulo_opuesto2 = sacar_angulo(nuevoLado3, nuevoLado1, lado2)
        if bolaX > hoyoX:
            x = bolaX - hoyoX
        else:
            x = hoyoX - bolaX
        if bolaY > hoyoY:
            y = bolaY - hoyoY
        else:
            y = hoyoY - bolaY

        if blancaX > hoyoX:
            x1 = blancaX - hoyoX
        else:
            x1 = hoyoX - blancaX
        if blancaY > hoyoY:
            y1 = blancaY - hoyoY
        else:
            y1 = hoyoY - blancaY


        if sacar_angulo(x, y, lado3) > sacar_angulo(x1, y1, lado2):
            print("hola1")
            angulo = sacar_angulo(y1, x1, lado2) + angulo_opuesto2
            if (bolaX < blancaX < hoyoX) or (bolaX > blancaX > hoyoX):
                if bolaY < blancaY:
                    if bolaX < blancaX:
                        print(-(180 - angulo))
                        return -(180 - angulo)
                    else:
                        print(-angulo)
                        return -angulo
                else:
                    if bolaX < blancaX:
                        print(180 - angulo)
                        return 180 - angulo
                    else:
                        print(180 - angulo)

                        return angulo

        elif (blancaY < bolaY < hoyoY) or (blancaY > bolaY > hoyoY):
            print("hola2")
            angulo = sacar_angulo(y1, x1, lado2) - angulo_opuesto2
        else:
            print("hola3")
            angulo = angulo_opuesto2 - sacar_angulo(y1, x1, lado2)


    if bolaY < blancaY:
        if bolaX > blancaX:
            print(-(180-angulo))
            return -(180-angulo)
        else:
            print(-angulo)
            return -angulo
    else:
        if bolaX > blancaX:
            print(180 - angulo)
            return 180-angulo
        else:
            print(180 - angulo)

            return angulo


def determinar_mejor_bola(balls, pockets, blanca, diam, window):
    distancia_Mejor = 1000000
    mejor_bola = 0
    mejor_pocket = 0
    index = 0
    index2 = 0
    for ball in balls:
        if index != len(balls)-1:
            index2 = 0
            for pocket in pockets:
                if se_puede(blanca.body.position.x, blanca.body.position.y, ball.body.position.x, ball.body.position.y, pocket[0], pocket[1], diam):
                    distancia_bola = sacar_hipotenusa_puntos(ball.body.position.x, ball.body.position.y, blanca.body.position.x, blanca.body.position.y)
                    distancia_hoyo = sacar_hipotenusa_puntos(ball.body.position.x, ball.body.position.y, pocket[0], pocket[1])
                    if distancia_bola + distancia_hoyo < distancia_Mejor:
                        distancia_Mejor = distancia_hoyo + distancia_bola
                        mejor_bola = index
                        mejor_pocket = index2
                index2 += 1
        index += 1
    return triangulo_de_tirada(blanca.body.position.x, blanca.body.position.y,
                        balls[mejor_bola].body.position.x, balls[mejor_bola].body.position.y, pockets[mejor_pocket][0],
                        pockets[mejor_pocket][1], diam,window)






