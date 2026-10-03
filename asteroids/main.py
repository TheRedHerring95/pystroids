import pygame
from constants import *
from logger import log_state
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
#    pygame.sprite.Group.add(updatable)
#    pygame.sprite.Group.add(drawable)
    while running == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            else:
                screen.fill("black")
                updatable.update(dt)
                for draw in drawable:
                    draw.draw(screen,LINE_WIDTH)
                pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(f"{dt}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
