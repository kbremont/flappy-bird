import pygame

class Bird:
    def __init__(self, screen_height):
        self.x = 50
        self.y = screen_height // 2
        self.vel = 0
        self.width = 34
        self.height = 24
        self.angle = 0
        bird_image = pygame.image.load("images/bird.png").convert_alpha()
        self.original_image = pygame.transform.scale(bird_image, (self.width, self.height))
        self.rotated_image = self.original_image

    def build_bird(self):
        return self.rotated_image.get_rect(center=(self.x, self.y))

    def flap(self, jump):
        self.vel = jump
        self.update_angle()
        self.rotated_image = pygame.transform.rotate(self.original_image, self.angle)

    def fall(self, gravity):
        self.vel += gravity
        self.y += self.vel
        self.update_angle()
        self.rotated_image = pygame.transform.rotate(self.original_image, self.angle)

    def update_angle(self):
        self.angle = -self.vel * 3
        self.angle = max(min(self.angle, 25), -90)

    def fall_to_ground(self, gravity, screen_height):
        while self.y + self.height < screen_height:
            self.vel += gravity
            self.y += self.vel
            self.update_angle()
            self.rotated_image = pygame.transform.rotate(self.original_image, self.angle)
            pygame.display.update()


        if self.y + self.height < screen_height:
            self.vel += 0.5
            self.y += self.vel
        else:
            self.y = screen_height - self.height