import sys
import pygame
from pygame.locals import *
import random as rand
from scipy import misc


pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('貪食蛇')
apple = pygame.image.load('apple.jpeg')
apple = pygame.transform.scale(apple, (20,20))
background = pygame.image.load('bulldog.jpg')
background = pygame.transform.scale(background, (640,480))
# print(apple.shape)
pink = pygame.Color(255, 182, 193)
blue = pygame.Color(0,0,200)
yellow = pygame.Color(200,200,0)
white = pygame.Color(255,255,255)
font = pygame.font.SysFont(None, 60)

gameover = font.render('gameover', True, white)
snake = [100,100]
snakeBody = [[100,100], [80,100], [60,100], [40,100], [20,100]]
food = [300,300]
foodRect = Rect(300, 300, 20, 20)
time_clock = pygame.time.Clock()
direction = 'right'
change = 'right'
dead = False
score = 0
while True:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                change = 'up'
            elif event.key == K_DOWN:
                change = 'down'
            elif event.key == K_RIGHT:
                change = 'right'
            elif event.key == K_LEFT:
                change = 'left'   
        elif event.type == MOUSEBUTTONDOWN:
            mouse = event.pos
            # print(foodRect, mouse)
            if foodRect.collidepoint(mouse):
                score += 1
                # print(mouse)
    direction = change
    if direction == 'right':
        snake[0] += 20
    elif direction == 'left':
        snake[0] -= 20
    elif direction == 'up':
        snake[1] -= 20
    elif direction == 'down':
        snake[1] += 20        
    snakeBody.insert(0, list(snake)) #加新的頭
    if snake[0] == food[0] and snake[1] == food[1]:
        #ate
        # print('ate')
        food[0] = rand.randint(0,31)*20
        food[1] = rand.randint(0,23)*20
        score += 1
    else:
        snakeBody.pop() #尾巴丟掉
    if snake[0] < 0 or snake[1] < 0 or snake[0] >= 640 or snake[1] >= 480:
        dead = True
    for i in range(1, len(snakeBody)):
        if snakeBody[i][0] == snake[0] and snakeBody[i][1] == snake[1]:
            dead = True
    # screen.fill((255, 255, 255))
    screen.blit(background, (0,0))
    text = font.render(str(score),True, blue)
    screen.blit(text, (0,0))
    for pos in snakeBody:
        pygame.draw.rect(screen, pink, Rect(pos[0], pos[1], 20, 20))
                                        #x  y    長  寬
    # pygame.draw.rect(screen, yellow, Rect(food[0]*20, food[1]*20, 20, 20))
    foodRect = Rect(food[0], food[1], 20, 20)
    screen.blit(apple, food)
    if dead:
        screen.fill((0,0,0))
        screen.blit(gameover, (screen.get_width()/2-60, screen.get_height()/2))

    pygame.display.flip()
    time_clock.tick(5)
    