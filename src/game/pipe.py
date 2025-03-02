import pygame
import random

class Pipe:
    def __init__(self):
        self.width = 70
        self.last_pipe = pygame.time.get_ticks()
        self.pipes = []
        self.image = pygame.image.load("images/pipe.png").convert_alpha()

    def build_pipe_pair(self, screen_height, screen_width, pipe_gap):
        gap_y = random.randint(100, screen_height - 100)
        top_pipe_rect = pygame.Rect(screen_width, 0, self.width, gap_y - pipe_gap // 2)
        bottom_pipe_rect = pygame.Rect(screen_width, gap_y + pipe_gap // 2, self.width, screen_height)
        top_pipe = {"rect": top_pipe_rect, "scored": False}
        bottom_pipe = {"rect": bottom_pipe_rect, "scored": False}
        self.pipes.extend([top_pipe, bottom_pipe])

    def draw_pipes(self, screen):
        for pipe in self.pipes:
            rect = pipe["rect"]
            # scale the pipe image to the size of the pipe rectangle
            scaled_pipe = pygame.transform.scale(self.image, (self.width, rect.height))
            # flip the top pipe image
            if rect.top == 0:
                scaled_pipe = pygame.transform.flip(scaled_pipe, False, True)
            screen.blit(scaled_pipe, (rect.x, rect.y))

    def move_pipes(self, pipe_speed):
        for pipe in self.pipes:
            pipe["rect"].x -= pipe_speed
        self.pipes = [pipe for pipe in self.pipes if pipe["rect"].x + self.width > 0]

    def check_collision(self, bird_rect, screen_height):
        for pipe in self.pipes:
            if bird_rect.colliderect(pipe["rect"]):
                return True
        if bird_rect.top <= 0 or bird_rect.bottom >= screen_height:
            return True
        return False