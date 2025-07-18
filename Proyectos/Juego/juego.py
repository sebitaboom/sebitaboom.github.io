import pygame
import parametros as p
from time import sleep
from personaje import Personaje
from weapons import Weapon
from os import listdir
from texto import DamageText
from items import Item


#Funciones
#Escalar imagen
def escalar_imagen(imagen: pygame.image, escala: int) -> pygame.image:
    w = imagen.get_width()
    h = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (w * escala, h * escala))
    return nueva_imagen

#Función contar elementos (recibe una carpeta y cuenta la cantidad de elementos)
def contar_elemento(path: str) -> int:
    return len(listdir(path))

#Función listar nombres elementos
def nombres_carpetas(path: str) -> list:
    return listdir(path)

#Función dibujar score
def dibujar_texto(texto: str, fuente, color: tuple, x: int, y: int) -> None:
    imagen = fuente.render(texto, True, color)
    ventana.blit(imagen, (x, y))

#Función poner los corazones
def vida_jugador() -> None:
    corazon_mitad_dibujado = False
    for i in range(5):
        if jugador.energia >= ((i + 1) * 20):
            ventana.blit(corazon_lleno, (5 + i * 40, 5))
        elif jugador.energia % 20 > 0 and not corazon_mitad_dibujado :
            ventana.blit(corazon_medio, (5 + i * 40, 5))
            corazon_mitad_dibujado = True
        else:
            ventana.blit(corazon_vacio, (5 + i * 40, 5))

#Iniciar juego
pygame.init()

#Ventana del juego y titulo del juego
ventana = pygame.display.set_mode(p.ANCHO_ALTO)
pygame.display.set_caption("La última derrota de Sebitaboom")

#Fuente del juego
font = pygame.font.Font("assets/fonts/80s-retro-future.ttf", p.ESCALA_FUENTE)

#Importar imagenes 
#Icono del juego
icono = pygame.image.load("assets/images/icono/icono.png")
pygame.display.set_icon(icono)

#Energía
corazon_vacio = pygame.image.load("C:/Users/sebas/Desktop/Repositorio/sebitaboom.github.io/Proyectos/Juego/assets/images/items/Corazon_1.png")
corazon_vacio = escalar_imagen(corazon_vacio, p.ESCALA_CORAZON)
corazon_medio = pygame.image.load("C:/Users/sebas/Desktop/Repositorio/sebitaboom.github.io/Proyectos/Juego/assets/images/items/Corazon_2.png")
corazon_medio = escalar_imagen(corazon_medio, p.ESCALA_CORAZON)
corazon_lleno = pygame.image.load("C:/Users/sebas/Desktop/Repositorio/sebitaboom.github.io/Proyectos/Juego/assets/images/items/Corazon_3.png")
corazon_lleno = escalar_imagen(corazon_lleno, p.ESCALA_CORAZON)




#Personajes
animaciones = []
for i in range(1, 5):
    imagen_personaje = pygame.image.load(f"assets/images/character/images/Neko-Walk-{i}.png.png")
    imagen_personaje = escalar_imagen(imagen_personaje, p.ESCALA_PERSONAJE)
    animaciones.append(imagen_personaje)

#Enemigos
path_enemigos = "assets/images/character/enemies"
tipo_enemigos = nombres_carpetas(path_enemigos)
animaciones_enemigos = []
for enemigo in tipo_enemigos:
    lista_temporal =  []
    path_temporal = f"assets/images/character/enemies/{enemigo}"
    numero_animaciones = contar_elemento(path_temporal)
    for indice in range(numero_animaciones):
        imagen_enemigo = pygame.image.load(f"{path_temporal}/{enemigo}_{indice + 1}.png")
        imagen_enemigo = escalar_imagen(imagen_enemigo, p.ESCALA_ENEMIGO)
        lista_temporal.append(imagen_enemigo)
    animaciones_enemigos.append(lista_temporal)



#Armas
imagen_rifle = pygame.image.load("assets/images/weapons/Rifle.png")
imagen_rifle = escalar_imagen(imagen_rifle, p.ESCALA_ARMA)

#Balas
imagen_balas = pygame.image.load("assets/images/weapons/Bala.png")
imagen_balas = escalar_imagen(imagen_balas, p.ESCALA_BALAS)


#Cargar imagenes de los items
posion_roja = pygame.image.load("assets/images/items/posion.png")
posion_roja = escalar_imagen(posion_roja, p.ESCALA_POSION)

coin_images = []
path_img = "assets/images/items/coins"
numero_coin_images = contar_elemento(path_img)

for i in range(numero_coin_images):
    imagen = pygame.image.load(f"assets/images/items/coins/coins_{i + 1}.png")
    imagen = escalar_imagen(imagen, p.ESCALA_MONEDA)
    coin_images.append(imagen)




#Crea un jugador de la clase personaje
jugador = Personaje(50, 100, animaciones, p.VIDA_PERSONAJE)


#Crea un enemigo de la clase personaje
enemigo_micha = Personaje(400, 400, animaciones_enemigos[0], p.VIDA_ENEMIGO)
enemigo_micha_c = Personaje(200, 150, animaciones_enemigos[1], p.VIDA_ENEMIGO)
enemigo_sam = Personaje(600, 200, animaciones_enemigos[2], p.VIDA_ENEMIGO)
enemigo_sam_c = Personaje(200, 300, animaciones_enemigos[3], p.VIDA_ENEMIGO)


#Lista de enemigos
lista_enemigos = []
lista_enemigos.append(enemigo_micha)
lista_enemigos.append(enemigo_sam)
lista_enemigos.append(enemigo_micha_c)
lista_enemigos.append(enemigo_sam_c)


#Crea un arma de la clase Weapon
rifle = Weapon(imagen_rifle, imagen_balas)


#Grupo de sprites
grupo_damage_text = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()

moneda = Item(350, 250, 0, coin_images)
posion = Item(250, 350, 1, [posion_roja])

grupo_items.add(moneda)
grupo_items.add(posion)


#Variables de movimientos del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

#Reloj (Controla los frames per second)
reloj = pygame.time.Clock()

#Correr juego
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

    if mover_derecha:
        delta_x = p.VELOCIDAD
    if mover_izquierda:
        delta_x = -p.VELOCIDAD
    if mover_arriba:
        delta_y = p.VELOCIDAD
    if mover_abajo:
        delta_y = -p.VELOCIDAD

    #Mover jugador
    jugador.movimiento(delta_x, delta_y) 

    #Actualizar el estado del jugador
    jugador.update()

    #Actualizar el estado del enemigo
    for enemigo in lista_enemigos:
        enemigo.update()
        #print(enemigo.energia) 


    #Actualizar el estado del arma
    bala = rifle.update(jugador)
    if bala:
        grupo_balas.add(bala)

    #Actualizar, hace que la bala dispare
    for balas in grupo_balas:
        damage, pos_damage = balas.update(lista_enemigos)
        if damage:
            damage_text = DamageText(pos_damage.centerx, pos_damage.centery, str(-damage), font, p.COLOR_ROJO)
            grupo_damage_text.add(damage_text)
    
    #Actualizar el daño
    grupo_damage_text.update()

    #Actualizar items
    grupo_items.update(jugador)
         
    #Dibujar el jugador
    jugador.dibujar(ventana)

    #Dibujar enemigos
    for enemigo in lista_enemigos:
        enemigo.dibujar(ventana)

    #Dibujar el arma
    rifle.dibujar(ventana)

    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

    #Dibujar los corazones
    vida_jugador()

    #Dibujar textos
    grupo_damage_text.draw(ventana)
    dibujar_texto(f"Score: {jugador.score}", font, p.COLOR_SCORE, 680, 5)  #Mejorar parámetros

    #Dibujar items
    grupo_items.draw(ventana)


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