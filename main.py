import pygame
from player import Player
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000  # Get delta time in seconds

        screen.fill("black")
        player.update(dt)  # Update player state
        player.draw(screen)  # Draw player
        pygame.display.flip()


if __name__ == "__main__":
    main()
