import parametros as p
from pygame import sprite, time



class Item(sprite.Sprite):
    def __init__(self, x: int, y: int, item_type: int, animacion_list: list) -> None:
        sprite.Sprite.__init__(self)
        #Define el tipo de objeto
        self.item_type = item_type #Por ahora 0 = monedas y 1 = pociones

        #Lista de animaciones de los objetos
        self.animacion_list = animacion_list

        #Índice de frame
        self.frame_index = 0

        #Ticks
        self.update_time = time.get_ticks()

        #Que imagen mostrar dado el frame
        self.image = self.animacion_list[self.frame_index]

        #¿Rectángulo?
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self, personaje) -> None:
        #Comprobar la colisión entre personae y los items
        if self.rect.colliderect(personaje.forma):
            #Monedas
            if self.item_type == 0:
                personaje.score += 1
            
            #Posiones
            elif self.item_type == 1:
                personaje.energia += 20
                
                if personaje.energia > 100:
                    personaje.energia = 100
            
            #Elimina la imagen
            self.kill()

        self.image = self.animacion_list[self.frame_index]

        if time.get_ticks() - self.update_time > p.COOLDOWN_ANIMACION:
            self.frame_index += 1
            self.update_time = time.get_ticks()
        
        if self.frame_index >= len(self.animacion_list):
            self.frame_index = 0
