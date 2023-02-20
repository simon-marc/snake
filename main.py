import pygame
from random import randrange
from settings import*

pygame.init()
pygame.mixer.init()

window_font = pygame.font.SysFont("Arialblack", 27)

snake_size = 10
snake_speed = 10

def display_score(score):
    score_text = window_font.render("Best Score : " +str(score), True, white)
    display.blit(score_text, [0,0])

def snake_icon(snake_size, segments):
    for segment in segments:
        pygame.draw.rect(display, blue, [segment[0], segment[1], snake_size, snake_size])

def game():

    game_over = False
    game_ended = False
    x = width / 2
    y = width / 2
    x_speed = 0
    y_speed = 0
    snake_length = 1
    segments = []
    target_x = round(randrange(0, width - snake_size) /10.0) * 10
    target_y = round(randrange(0, height - snake_size) /10.0) * 10

    while not game_over:

        while game_ended:

            display.fill(darkgrey)
            game_over_msg_1 = window_font.render("YOU LOST !", True, yellow)
            game_over_msg_2 = window_font.render("Press spacebar to reset game !", True, yellow)
            game_over_msg_3 = window_font.render("Press ESC to quit !", True, yellow)
            display.blit(game_over_msg_1, [width / 3, height / 3])
            display.blit(game_over_msg_2, [width / 3 - 70, height / 3 + 30])
            display.blit(game_over_msg_3, [width / 3 - 35, height / 3 + 60])

            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_ended = False
                    elif event.key == pygame.K_SPACE:
                        game()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_ended = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        if x>= width or x < 0 or y >= height or y < 0:
            game_ended = True
    
        x += x_speed
        y += y_speed

        display.fill(darkgrey)
        pygame.draw.rect(display, yellow, [target_x, target_y, snake_size, snake_size])
        segments.append([x, y])

        if len(segments) > snake_length:
            del segments[0]

        for segment in segments[:-1]:
            if segment == [x,y]:
                game_ended = True

        snake_icon(snake_size, segments)
        display_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(randrange(0, width - snake_size) /10.0) * 10
            target_y = round(randrange(0, height - snake_size) /10.0) * 10

            snake_length += 1
        clock.tick(snake_speed)

    pygame.quit()

game()

