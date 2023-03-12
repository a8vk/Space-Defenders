import  pygame  # pip install pygame
import controls
from gun import Gun
from pygame.sprite import Group
from ino import Ino

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    ino = Ino(screen)


    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, ino, bullets)
        controls.update_bullets(bullets)

run()