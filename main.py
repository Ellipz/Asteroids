# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main () :
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    print ("Starting asteroids!")
    #print (f"Screen width: {SCREEN_WIDTH}")
    #print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.collision(player) == True:
                sys.exit("Game over!")
        
            for shot in shots:
                if shot.collision(obj) == True:
                    shot.kill()
                    obj.split()

        pygame.Surface.fill(screen,(0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        

        # limit the framerate to 144 FPS
            #clock.tick(144)
        dt = clock.tick(144)/1000
        

if __name__ == "__main__":
    main()