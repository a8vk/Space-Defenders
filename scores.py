import pygame.font

class Scores():
    """Вывод игровой информации"""
    def __init__(self, screen, stats):
        """Инициализируем подсчёт очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = 51, 204, 0
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()

    def image_score(self):
        """Преобразовывает текст счёта в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.score_rect.right + 40
        self.score_rect.top = 20

    def show_score(self):
        """Вывод счёта на экран"""
        self.screen.blit(self.score_img, self.score_rect)