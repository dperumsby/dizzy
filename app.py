import sys
import pygame as pg


pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()


class Dizzy:

    STILL_FRAMES = [
        pg.image.load('assets/dizzy-still-0.png').convert(),
        pg.image.load('assets/dizzy-still-1.png').convert()
    ]

    WALKING_FRAMES_LEFT = [
        pg.image.load('assets/dizzy-walk-left-1.png').convert(),
        pg.image.load('assets/dizzy-walk-left-2.png').convert(),
        pg.image.load('assets/dizzy-walk-left-3.png').convert(),
        pg.image.load('assets/dizzy-walk-left-4.png').convert(),
        pg.image.load('assets/dizzy-walk-left-5.png').convert(),
        pg.image.load('assets/dizzy-walk-left-6.png').convert(),
        pg.image.load('assets/dizzy-walk-left-7.png').convert()
    ]

    WALKING_FRAMES_RIGHT = [
        pg.image.load('assets/dizzy-walk-right-1.png').convert(),
        pg.image.load('assets/dizzy-walk-right-2.png').convert(),
        pg.image.load('assets/dizzy-walk-right-3.png').convert(),
        pg.image.load('assets/dizzy-walk-right-4.png').convert(),
        pg.image.load('assets/dizzy-walk-right-5.png').convert(),
        pg.image.load('assets/dizzy-walk-right-6.png').convert(),
        pg.image.load('assets/dizzy-walk-right-7.png').convert()
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = self.STILL_FRAMES[0]
        self.rect = self.surface.get_rect(center=(self.x, self.y))
        self.animation_index = 0

    def animate_walk(self, left, right):        
        if left:
            frames = self.WALKING_FRAMES_LEFT

        elif right:
            frames = self.WALKING_FRAMES_RIGHT

        else:
            frames = self.STILL_FRAMES

        if self.animation_index >= len(frames):
            self.animation_index = 0

        self.surface = frames[self.animation_index]
        self.rect = self.surface.get_rect(center=(self.x, self.y))


DIZZY_FRAME = pg.USEREVENT
pg.time.set_timer(DIZZY_FRAME, 200)

dizzy = Dizzy(400, 300)

while True:
    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == DIZZY_FRAME:
            dizzy.animation_index += 1

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        dizzy.x += 1
        dizzy.animate_walk(left=False, right=True)
    elif keys[pg.K_LEFT]:
        dizzy.x -= 1
        dizzy.animate_walk(left=True, right=False)
    else:
        dizzy.animate_walk(left=False, right=False)

    screen.blit(dizzy.surface, dizzy.rect)


    pg.display.update()
    clock.tick(120)
