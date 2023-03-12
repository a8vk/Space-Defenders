import pygame
import sys
import time
from bullet import Bullet
from ino import Ino


def events(screen, gun, bullets):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            # пробел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, gun, inos, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(inos, bullets):
    """Обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)


def gun_kill(stats, screen, gun, inos, bullets):
    """Столкновение пушки и армии"""
    stats.guns_left -= 1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    gun.create_gun()
    time.sleep(2)


def update_inos(stats, screen, gun, inos, bullets):
    """Обновляет позицию пришельце"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets)


def create_army(screen, inos):
    """Создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    numbers_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    numbers_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_numer in range(numbers_ino_y-3):
        for ino_number in range(numbers_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_numer)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_numer)
            inos.add(ino)
