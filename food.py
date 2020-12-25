from random import randint
import pygame


class Food:
    def __init__(self, w, rows):
        self.r = None
        self.c = None
        self.w = w
        self.rows = rows
        self.color = (255, 129, 0)
        self.food_on_map = False

    def update_food(self, grid):
        index_col = randint(0, self.rows - 1)
        index_row = randint(0, self.rows - 1)
        self.r = grid[index_row][index_col][0]
        self.c = grid[index_row][index_col][1]


    def food_location(self):
        return [self.r, self.c, self.w]

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.r, self.c, self.w, self.w))

