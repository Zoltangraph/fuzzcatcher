# Example file showing a circle moving on screen
from random import randint

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((780, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() -200)
playerimage = pygame.image.load("cippert.png").convert_alpha()
playerimage = pygame.transform.scale(playerimage , (100,100))

soda_pos = pygame.Vector2(screen.get_width() / 2, -50)
soda = pygame.image.load("soda.png").convert_alpha()
soda = pygame.transform.scale(soda , (100,100))

points = 0

font = pygame.font.SysFont(None, 50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
    
    playerRect = playerimage.get_rect(center = player_pos)
    screen.blit(playerimage, playerRect)
    
    sodaRect = soda.get_rect(center = soda_pos)
    screen.blit(soda, sodaRect)
    soda_pos.y += 10 


    if playerRect.colliderect(sodaRect):
        soda_pos.y = -50
        soda_pos.x = randint(0, 780)
        points += 1
    
    
    pointText = font.render(str(points), True, "white")
    screen.blit(pointText, (50, 50))
    
    
    if soda_pos.y > screen.get_height():
        soda_pos.y = -50
        soda_pos.x = randint(0, 1280)
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()