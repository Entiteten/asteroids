import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    print("Starting Asteroids!")
    print((f"Screen width: {SCREEN_WIDTH}"))
    print((f"Screen height: {SCREEN_HEIGHT}"))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)


    while True:
        clock.tick(60)
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
