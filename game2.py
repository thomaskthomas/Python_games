import pygame as pg
import random

pg.init()
window_width=800
window_height=600
screen=pg.display.set_mode((window_width, window_height))
pg.display.set_caption("My Game")
clock=pg.time.Clock()
running=True
#defining font 
sys_font=pg.font.SysFont("Impact", 80)
#render text
sys_font=sys_font.render("Hell World", True, "Red")
#text_rect
sys_font_rect=sys_font.get_rect()
#position of text
sys_font_rect.center=(window_width//2, window_height//2)

#adding hero
hero=pg.image.load("hero_right.png")
#get srrounding of hero
hero_rect=hero.get_rect()
#position of her0=
hero_rect.topleft=(0,0)

dt=0
player_pos=pg.Vector2(screen.get_width()//2, screen.get_height()//2)
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    screen.fill((0, 0, 0))
    #putting hero on the screen
    pg.draw.rect(screen,"blue",hero_rect,1)
    screen.blit(hero, hero_rect)
    #putting text on the screen
    pg.draw.rect(screen,"red",sys_font_rect,1 )
    screen.blit(sys_font, sys_font_rect)
    #pg.draw.circle(screen,"blue",player_pos,40)
    key=pg.key.get_pressed()
    #restricting the movement of hero within the window
    if key[pg.K_w] and hero_rect.y>0:
        hero_rect.y-=200*dt
    if key[pg.K_s] and hero_rect.y<window_height-hero_rect.height:
        hero_rect.y+=200*dt
    if key[pg.K_a] and hero_rect.x>0:
        hero_rect.x-=200*dt
    if key[pg.K_d] and hero_rect.x<window_width-hero_rect.width:
        hero_rect.x+=200*dt
    #adding Mouse movement
    if pg.mouse.get_pressed()[0]:
        if event.type==pg.MOUSEMOTION:
            pos=pg.mouse.get_pos()
            hero_rect=pg.Vector2(pos)
    #adding collison
    if hero_rect.colliderect(sys_font_rect):
        sys_font_rect.x=random.randint(0,window_width-sys_font_rect.width)
        sys_font_rect.y=random.randint(0,window_height-sys_font_rect.height)
    
    #if event.type==pg.MOUSEBUTTONUP:
        #pos=pg.mouse.get_pos()
        #player_pos=pg.Vector2(pos)
    pg.display.flip()
    dt=clock.tick(60)/1000



pg.quit()