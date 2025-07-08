import pygame
import parametros as p 
from math import (degrees, atan2, cos, radians, sin)
from personaje import Personaje

#Terminar
def max_min(angulo: float, maximo: float, minimo: float) -> float:
    if min(angulo, maximo) ==  maximo:
        return maximo
    elif max(angulo, minimo) == minimo:
        return minimo
    else:
        return angulo



#Clase de las balas
class Bullet(pygame.sprite.Sprite):
    def __init__(self, imagen: pygame.image, x: float, y: float, angulo: float) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = imagen
        self.angulo = angulo
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        #calculo ela velocidad
        self.delta_x = cos(radians(self.angulo)) * p.VELOCIDAD_BALA
        self.delta_y = - sin(radians(self.angulo)) * p.VELOCIDAD_BALA

    def update(self) -> None:
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        #Ver si las balas salieron de la pantalla
        if self.rect.right < 0 or self.rect.left > p.ANCHO or self.rect.bottom < 0 or self.rect.top > p.ALTO:
            self.kill()

    #Dibujar y posiciona donde sale la bala
    def dibujar(self, ventana: pygame.display) -> None:
        ventana.blit(self.image, (self.rect.centerx + int(self.image.get_width() / 2), 
                                  self.rect.centery - int(self.image.get_height() / 2)))



#Clase armas
class Weapon:
    def __init__(self, imagen_arma: pygame.image, imagen_bala: pygame.image) -> None:
        self.imagen_original= imagen_arma
        self.angulo = p.ANGULO_INICIAL
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.imagen_bala = imagen_bala
        self.forma = self.imagen.get_rect()
        self.dispara = False
        self.ultimo_disparo = pygame.time.get_ticks()


    def update(self, personaje: Personaje) -> Bullet:
        disparo_cooldown = p.TIEMPO_BALA
        bala = None

        #centrando el arma en el centro del personaje
        self.forma.center = personaje.forma.center

        #Hace que el arma siga la dirección del jugador
        if not personaje.flip:
            self.forma.x += personaje.forma.width * p.ESCALA_X
            self.forma.y += personaje.forma.height * p.ESCALA_Y
            self.rotar_arma(False)

        else:         
            self.forma.x -= personaje.forma.width * p.ESCALA_X
            self.forma.y += personaje.forma.height * p.ESCALA_Y
            self.rotar_arma(True)

        #Mover el rifle siguiendo el mouse
        mouse_posicion = pygame.mouse.get_pos()
        distancia_x = mouse_posicion[0] - self.forma.centerx
        distancia_y = -(mouse_posicion[1] - self.forma.centery)
        self.angulo = degrees(atan2(distancia_y, distancia_x))


 
        #DEFINIR MAX Y MIN (TAREA)
        #print((self.angulo))

        #Detectar los clicks del mouse
        if pygame.mouse.get_pressed()[0] and not self.dispara and (pygame.time.get_ticks() - self.ultimo_disparo >= disparo_cooldown):
            bala =  Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.dispara = True
            self.ultimo_disparo = pygame.time.get_ticks()
        #resetear el click del mouse
        if not pygame.mouse.get_pressed()[0]:
            self.dispara = False
        return  bala



    def rotar_arma(self, rotar: bool) -> None:
        if rotar:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original, False, False) 
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
             
    def dibujar(self, ventana: pygame.display) -> None:
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)


        ventana.blit(self.imagen, self.forma)
        #pygame.draw.rect(ventana, p.COLOR_ARMA, self.forma, width = 1)


