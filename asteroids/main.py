import pygame
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (drawable,updatable,shots)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    field = AsteroidField()
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
        for asteroid in asteroids:
            hit = asteroid.collides_with(player)
            if hit == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        dt = clock.tick(60) / 1000
#        print(f"{dt}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
