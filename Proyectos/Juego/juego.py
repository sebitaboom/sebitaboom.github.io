import pygame
import parametros as p
from time import sleep
from personaje import Personaje
from weapons import Weapon

pygame.init()
ventana = pygame.display.set_mode((p.ANCHO, p.ALTO))
pygame.display.set_caption("La derrota de sebitaboom")


#Funcion escalar imagen
def escalar_imagen(imagen: pygame.image, escala: int) -> pygame.image:
    w = imagen.get_width()
    h = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (w * escala, h * escala))
    return nueva_imagen

#Importar imagenes 



#Personajes
animaciones = []
for i in range(1, 5):
    imagen_personaje = pygame.image.load(f"assets/images/character/images/Neko-Walk-{i}.png.png")
    imagen_personaje = escalar_imagen(imagen_personaje, p.ESCALA_PERSONAJE)
    animaciones.append(imagen_personaje)
#Armas
imagen_rifle = pygame.image.load("assets/images/weapons/Auto_Rifle-SciFi.png")
imagen_rifle = escalar_imagen(imagen_rifle, p.ESCALA_ARMA)

#Balas
imagen_balas = pygame.image.load("assets/images/weapons/bullets_PNG35509.png")
imagen_balas = escalar_imagen(imagen_balas, p.ESCALA_BALAS)



#Crea un jugador de la clase personaje
jugador = Personaje(50, 50, animaciones)

#Crea un arma de la clase Weapon
rifle = Weapon(imagen_rifle, imagen_balas)


#Grupo de sprites
grupo_balas = pygame.sprite.Group()


#Variables de movimientos del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

#Reloj (Controla los frames per second)
reloj = pygame.time.Clock()

#Correo o no
run = True




#Evento de todos los juego
while run:
    #Que vaya 60 fps 
    reloj.tick(p.FPS)
    

    #Rellena el fondo de un color azul
    ventana.fill(p.COLOR_BG)


    #Calcular movimiento del jugador:
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = p.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -p.VELOCIDAD
    if mover_arriba == True:
        delta_y = p.VELOCIDAD
    if mover_abajo == True:
        delta_y = -p.VELOCIDAD

    #Mover jugador
    jugador.movimiento(delta_x, delta_y) 
    #Actualizar el estado del jugador
    jugador.update()

    #Actualiza el estado del arma
    bala = rifle.update(jugador)
    if bala:
        grupo_balas.add(bala)

    #Hace que la bala dispara  
    for balas in grupo_balas:
        balas.update()   
    print(grupo_balas)

    #Dibujar el jugador
    jugador.dibujar(ventana)

    #Dibujar el arma
    rifle.dibujar(ventana)


    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)


    for evento in pygame.event.get():
        #Cerrar el juego
        if evento.type == pygame.QUIT:
            run = False

        #KEYDOWN es si apreto una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                mover_izquierda = True

            elif evento.key == pygame.K_d:
                mover_derecha = True

            elif evento.key == pygame.K_w:
                mover_abajo = True

            elif evento.key == pygame.K_s:
                mover_arriba = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a:
                mover_izquierda = False

            elif evento.key == pygame.K_d:
                mover_derecha = False

            elif evento.key == pygame.K_w:
                mover_abajo = False

            elif evento.key == pygame.K_s:
                mover_arriba = False

    pygame.display.update()

    
pygame.quit()