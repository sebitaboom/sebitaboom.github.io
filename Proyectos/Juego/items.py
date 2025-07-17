from pygame import sprite, time


class Item(sprite.Sprite):
    def __init__(self, x: int, y: int, item_type: int, animacion_list: list) -> None:
        sprite.Sprite.__init__(self)
        self.item_type = item_type #Por ahora 0 = monedas y 1 = pociones
        self.animacion_list = animacion_list
        self.frame_index = 0
        self.update_time = time.get_ticks()
        self.image = self.animacion_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect = (x, y)


    def update(self) -> None:
        cooldown_animacion = 150
        self.image = self.animacion_list[self.frame_index]

        if time.get_ticks() - self.update_time > cooldown_animacion:
            self.frame_index += 1
            self.update_time = time.get_ticks()
        
        if self.frame_index >= len(self.animacion_list):
            self.frame_index = 0
