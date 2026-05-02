import pygame
pygame.init()

Window_width=800
Window_height=600
screen=pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption("Space Game")



running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0, 0, 0))
            
    pygame.display.update()
    
    
    
    





pygame.quit()