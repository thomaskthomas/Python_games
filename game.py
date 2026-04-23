import pygame as pg

pg.init()
screen=pg.display.set_mode((400, 300))
pg.display.set_caption("My Game")
clock=pg.time.Clock()
running=True

dt=0
player_pos=pg.Vector2(screen.get_width()//2, screen.get_height()//2)
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    screen.fill((0, 0, 0))
    pg.draw.circle(screen,"blue",player_pos,40)
    key=pg.key.get_pressed()
    if key[pg.K_w]:
        player_pos.y-=200*dt
    if key[pg.K_s]:
        player_pos.y+=200*dt
    if key[pg.K_a]:
        player_pos.x-=200*dt
    if key[pg.K_d]:
        player_pos.x+=200*dt
    pg.display.flip()
    dt=clock.tick(60)/1000



pg.quit()