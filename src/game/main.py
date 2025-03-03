import pygame
import sys
from bird import Bird
from pipe import Pipe
from score import Score

# Screen dimensions and game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5
BIRD_JUMP = -10
PIPE_SPEED = 3
PIPE_GAP = 150
PIPE_FREQUENCY = 1500


# Set up the display and clock
def build_window():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    background_image = pygame.image.load("images/background.png").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    return screen, clock, background_image

def main():
    pygame.init()

    screen, clock, background_image = build_window()
    bird = Bird(SCREEN_HEIGHT)
    pipe = Pipe()
    score = Score(bird, pipe)
    playing = True

    # main game loop
    while True:
        # draw background, bird, and pipes
        screen.blit(background_image, (0, 0))
        screen.blit(bird.rotated_image, (bird.x, bird.y))
        pipe.draw_pipes(screen)

        if playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Bird "flap" when space is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap(BIRD_JUMP)

            # update bird physics
            bird.fall(GRAVITY)
            bird_rect = bird.build_bird()

            # create new pipes based on time frequency
            current_time = pygame.time.get_ticks()
            if current_time - pipe.last_pipe > PIPE_FREQUENCY:
                pipe.last_pipe = current_time
                pipe.build_pipe_pair(SCREEN_HEIGHT, SCREEN_WIDTH, PIPE_GAP)

            # move pipes
            pipe.move_pipes(PIPE_SPEED)

            # check for collision
            if pipe.check_collision(bird_rect, SCREEN_HEIGHT):
                bird.fall_to_ground(GRAVITY, SCREEN_HEIGHT)
                score.end_game()
                playing = False

            # update score
            score.update_score()

            # display the score in top left corner
            score.display_score(screen)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pipe.pipes.clear()
                        bird.y = SCREEN_HEIGHT // 2
                        bird.vel = 0
                        bird.angle = 0
                        playing = True

            # display high score
            score.display_high_score(screen, SCREEN_WIDTH, SCREEN_HEIGHT)


        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()