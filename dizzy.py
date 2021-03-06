import pygame as pg


class Dizzy:

    STILL_1 = pg.image.load('assets/dizzy-still-1.png').convert()
    STILL_2 = pg.image.load('assets/dizzy-still-2.png').convert()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation_index = 0

    def animate_still(self):
        if self.animation_index >= 2:
            self.animation_index = 0

        frames = [self.STILL_1, self.STILL_2]
        surface = frames[self.animation_index]
        rect = surface.get_rect(center=(self.x, self.y))
        return surface, rect

