from pygame import sprite, image

class DamageText(sprite.Sprite):
    def __init__(self, x: int, y: int, damage: str, font: image, color) -> None:
        sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.contador = 0

    def update(self) -> None:
        self.rect.y -= 2
        self.contador += 1
        if self.contador > 50:
            self.kill()