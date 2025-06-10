import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kouka_img = pg.image.load("fig/3.png")
    kouka_img = pg.transform.flip(kouka_img,True,False)
    tmr = 0
    x = tmr % 3200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600,0])  #2枚目
        screen.blit(bg_img, [-x + 3200, 0])  #3枚目
        screen.blit(kouka_img,[300,200])
        pg.display.update()
        x += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()