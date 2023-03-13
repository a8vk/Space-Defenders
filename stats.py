class Stats():
    """Отслеживание статистики"""

    def __init__(self):
        """Инициализирует статистику"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """Статистика изменяющаяся во время игры"""
        self.guns_left = 2
