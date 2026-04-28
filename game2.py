import pygame as pg

pg.init()
window_width=400
window_height=300
screen=pg.display.set_mode((window_width, window_height))
pg.display.set_caption("My Game")
clock=pg.time.Clock()
running=True
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
    screen.blit(hero, hero_rect)
    #pg.draw.circle(screen,"blue",player_pos,40)
    key=pg.key.get_pressed()
    if key[pg.K_w]:
        hero_rect.y-=200*dt
    if key[pg.K_s]:
        hero_rect.y+=200*dt
    if key[pg.K_a]:
        hero_rect.x-=200*dt
    if key[pg.K_d]:
        hero_rect.x+=200*dt
    #adding Mouse movement
    if pg.mouse.get_pressed()[0]:
        if event.type==pg.MOUSEMOTION:
            pos=pg.mouse.get_pos()
            hero_rect=pg.Vector2(pos)
    
    #if event.type==pg.MOUSEBUTTONUP:
        #pos=pg.mouse.get_pos()
        #player_pos=pg.Vector2(pos)
    pg.display.flip()
    dt=clock.tick(60)/1000



pg.quit()