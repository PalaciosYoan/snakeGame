import pygame, sys

from grid import Grid
from snake import Snake
from food import Food

pygame.init()
WIDTH = 800
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
CLOCK = pygame.time.Clock()
SNAKE_SPEED = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)


def your_score(score, highScore):
    score = SCORE_FONT.render("Your Final Score is " + str(score), True, BLACK)
    HS = SCORE_FONT.render("Highest Score is " + str(highScore), True, BLACK)
    reset = SCORE_FONT.render("(pressed 'r' to reset)", True, BLACK)
    WIN.blit(score, [0, 0])
    WIN.blit(HS, [0, 30])
    WIN.blit(reset, [0, 60])


def draw(grid, food, snake):
    WIN.fill(WHITE)
    grid.draw(WIN)
    food.draw(WIN)
    snake.draw(WIN)
    pygame.display.update()


def eaten_food(snake, food, w):
    return snake[0] >= food[0] and snake[0] + w <= food[0] + w and snake[1] >= food[1] and snake[1] + w <= food[1] + w


def main():
    rows = 32
    grid = Grid(rows, WIDTH)
    snake = Snake(300, 300, WIDTH // rows, grid.get_grid())
    food = Food(WIDTH // rows, rows)
    direction = "right"
    gameover = False
    highest_score = 0
    food.update_food(grid.get_grid())

    while True:
        draw(grid, food, snake)
        snake.direction(direction)
        if snake.collision_with_tail():
            gameover = True
        if not gameover and not (
                snake.snake_head()[0] > WIDTH or snake.snake_head()[1] < 0 or snake.snake_head()[0] < 0 or
                snake.snake_head()[1] > HEIGHT):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        direction = "left"
                    elif event.key == pygame.K_d:
                        direction = "right"
                    elif event.key == pygame.K_w:
                        direction = "up"
                    elif event.key == pygame.K_s:
                        direction = "down"
            if eaten_food(snake.snake_head(), food.food_location(), food.food_location()[2]):
                food.update_food(grid.get_grid())
                snake.grow()
            CLOCK.tick(SNAKE_SPEED)
        else:
            if \
                    snake.snake_head()[0] > WIDTH or snake.snake_head()[1] < 0 or snake.snake_head()[0] < 0 or \
                            snake.snake_head()[1] > HEIGHT:
                gameover = True
            while gameover:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            snake.reset()
                            food.update_food(grid.get_grid())
                            gameover = False
                if highest_score < snake.length() - 1:
                    highest_score = snake.length() - 1
                your_score(snake.length() - 1, highest_score)
                pygame.display.update()


if __name__ == "__main__":
    main()
