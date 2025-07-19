import pygame
import parametros as p


class Personaje:
    def __init__(self, x: int, y: int, animaciones: list, energia: int) -> None: 
        #Score del personaje
        self.score = 0


        #Vida del personaje
        self.energia = energia

        #Vivo o muerto
        self.vivo = True
        #Voltear
        self.flip = False

        #Animaciones y frames
        self.animaciones = animaciones
        self.frame_index = 0

        #Almacena los ms despues de que inicio
        self.update_time = pygame.time.get_ticks()

        #Imagen
        self.image = animaciones[self.frame_index]

        #Forma del personaje
        self.forma = self.image.get_rect()
        #Donde se va a encontrar
        self.forma.center = (x, y)
        
    def update(self) -> None:
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False




        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= p.COOLDOWN_ANIMACION_PERSONAJE:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

        

    def dibujar(self, ventana: pygame.display) -> None:
        #Voltea la imagen
        image_flip = pygame.transform.flip(self.image, self.flip, False)

        ventana.blit(image_flip, self.forma)
        #pygame.draw.rect(ventana, p.COLOR_PERSONAJE, self.forma, width = 1)
 
    def movimiento(self, delta_x: int, delta_y: int) -> None:
        if delta_x < 0:
            self.flip = True
        if delta_x >0:
            self.flip = False

        self.forma.x += delta_x
        self.forma.y += delta_y