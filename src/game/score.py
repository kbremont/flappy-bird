import pygame

class Score:
    def __init__(self, bird, pipe):
        self.score = 0
        self.high_score = 0
        self.previous_score = 0
        self.bird = bird
        self.pipe = pipe

    def update_score(self):
        for pipe in self.pipe.pipes:
            rect = pipe["rect"]
            if rect.x + rect.width < self.bird.x and not pipe["scored"]:
                pipe["scored"] = True
                self.score += 0.5

    def display_score(self, screen):
        font = pygame.font.SysFont(None, 36)
        text = font.render("Score: " + str(int(self.score)), True, (255, 255, 255))
        screen.blit(text, (10, 10))

    def end_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.previous_score = self.score
        self.score = 0

    def display_high_score(self, screen, screen_width, screen_height):
        font = pygame.font.SysFont(None, 36)

        high_score_text = font.render("High Score: " + str(int(self.high_score)), True, (255, 255, 255))
        high_score_text_rect = high_score_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(high_score_text, high_score_text_rect)

        previous_score_text = font.render("Previous Score: " + str(int(self.previous_score)), True, (255, 255, 255))
        previous_score_text_rect = previous_score_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(previous_score_text, previous_score_text_rect)

        keep_playing_text = font.render("Press SPACE to keep playing", True, (255, 255, 255))
        keep_playing_text_rect = keep_playing_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(keep_playing_text, keep_playing_text_rect)
