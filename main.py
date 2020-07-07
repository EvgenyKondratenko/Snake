# Copyright 2020 Evgeny Kondratenko
import pygame
import random


# settings
W = 800
H = 600
SIZE = 25
FPS = 5
orange, black, green, red = (
    (255, 120, 10),
    (0,   0,   0),
    (0,   255, 0),
    (255, 0,   0)
)

# init
clock = pygame.time.Clock()
pygame.init()
font_score = pygame.font.SysFont('Arial', 30, bold=True)
font_game_over = pygame.font.SysFont('Arial', 50, bold=True)
board = pygame.display.set_mode([W, H])
pygame.display.set_caption('Snake')
x,  y = random.randrange(0, W - SIZE, SIZE), random.randrange(0, H - SIZE, SIZE)
apple = random.randrange(0, W - SIZE, SIZE), random.randrange(0, H - SIZE, SIZE)
snake = [(x, y)]
dx, dy = 0, 0
length = 1


def close():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()


# main loop
score = 0
state = True
while state:
    board.fill(black)
    pygame.draw.rect(board, red, (apple[0], apple[1], SIZE, SIZE))
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    print(snake)
    # draw snake
    for i, j in snake:
        pygame.draw.rect(board, green, (i, j, SIZE - 1, SIZE - 1))
    # score
    render_score = font_score.render(f'Your score: {score}', 1, pygame.Color('orange'))
    board.blit(render_score, (5, 5))
    pygame.display.update()
    # eating apple
    if (x, y) == apple:
        print('hello')
        while apple in snake:
            apple = random.randrange(0, W - SIZE, SIZE), random.randrange(0, H - SIZE, SIZE)
            print('new coordinates = ', apple)
        score += 1
        length += 1
    # borders
    if x < 0 or x >= W or y < 0 or y >= H or len(snake) != len(set(snake)):
        state = False
    # press ESC or close by mouse to quit
    close()
    # controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if dx != 1:
            dx, dy = -1, 0
    elif keys[pygame.K_RIGHT]:
        if dx != -1:
            dx, dy = 1, 0
    elif keys[pygame.K_UP]:
        if dy != 1:
            dx, dy = 0, -1
    elif keys[pygame.K_DOWN]:
        if dy != -1:
            dx, dy = 0, 1

    clock.tick(FPS)


while True:
    render_game_over = font_game_over.render('GAME OVER', 1, pygame.Color('orange'))
    board.blit(render_game_over, (W // 2 - 150, H // 3))
    pygame.display.flip()
    close()
