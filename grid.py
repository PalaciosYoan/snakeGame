import pygame


class Grid:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.cubeSize = width // rows
        self.grid = []
        for r in range(rows):
            temp = []
            for c in range(rows):
                temp.append([r*self.cubeSize, c*self.cubeSize, self.cubeSize])
            self.grid.append(temp)
        self.color = (190, 190, 190)

    def draw(self, window):
        for r in range(self.rows):
            pygame.draw.line(window, self.color, (0, r * self.cubeSize), (self.width, r * self.cubeSize))
            for c in range(self.rows):
                pygame.draw.line(window, self.color, (c * self.cubeSize, 0), (c * self.cubeSize, self.width))

    def get_grid(self):
        return self.grid
