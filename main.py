
import pygame


pygame.init()

Window = pygame.display.set_mode(size = (600, 480))
print('Setup end')

print('Setup start')

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #end pygame
