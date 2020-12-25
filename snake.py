import pygame


class Snake:
    def __init__(self, x, y, width, grid):
        self.x = x
        self.y = y
        self.width = width
        self.tail = [[self.x, self.y, "right"]]
        self.grid = grid
        self.color = (0, 255, 0)

    def grow(self):
        direction = self.tail[-1][2]
        if direction == "up":
            self.tail.append([self.tail[-1][0], self.tail[-1][1] + self.width, self.tail[-1][2]])
        elif direction == "down":
            self.tail.append([self.tail[-1][0], self.tail[-1][1] - self.width, self.tail[-1][2]])
        elif direction == "left":
            self.tail.append([self.tail[-1][0] + self.width, self.tail[-1][1], self.tail[-1][2]])
        elif direction == "right":
            self.tail.append([self.tail[-1][0] - self.width, self.tail[-1][1], self.tail[-1][2]])

    def collision_with_tail(self):
        for i in range(2, len(self.tail), 1):
            if (self.tail[0][2] == "up" and
                    self.tail[i][0] <= self.tail[0][0] <= self.tail[i][0] + self.width and
                    self.tail[i][1] <= self.tail[0][1] <= self.tail[i][1] + self.width
            ):
                return True

            elif (self.tail[0][2] == "down" and
                  self.tail[i][0] <= self.tail[0][0] <= self.tail[i][0] + self.width and
                  self.tail[i][1] <= self.tail[0][1] + self.width <= self.tail[i][1] + self.width
            ):
                return True

            elif (self.tail[0][2] == "left" and
                  self.tail[i][0] <= self.tail[0][0] <= self.tail[i][0] + self.width and
                  self.tail[i][1] <= self.tail[0][1] <= self.tail[i][1] + self.width
            ):
                return True

            elif (self.tail[0][2] == "right" and
                  self.tail[i][0] <= self.tail[0][0] + self.width <= self.tail[i][0] + self.width and
                  self.tail[i][1] <= self.tail[0][1] <= self.tail[i][1]
            ):
                return True

        return False

    def length(self):
        return len(self.tail)

    def reset(self):
        self.tail = [[self.x, self.y, "right"]]

    def direction(self, dir):
        self.tail[0][2] = dir
        if dir == "right":
            self.tail[0][0] += self.width
        elif dir == "left":
            self.tail[0][0] -= self.width
        elif dir == "down":
            self.tail[0][1] += self.width
        elif dir == "up":
            self.tail[0][1] -= self.width

        for i in range(len(self.tail) - 1, 0, -1):
            self.tail[i][0] = self.tail[i - 1][0]
            self.tail[i][1] = self.tail[i - 1][1]
            self.tail[i][2] = self.tail[i - 1][2]

    def snake_head(self):
        return self.tail[0]

    def draw(self, win):
        for body in self.tail:
            pygame.draw.rect(win, self.color, (body[0], body[1], self.width, self.width))
