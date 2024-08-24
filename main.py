import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for element in updatable:
            element.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                exit()

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # limit fps to 60


if __name__ == "__main__":
    main()
