import pygame
from pygame.locals import *


def parallaxe(window, image, position_x, speed):
    window.blit(image, (position_x, 0))
    return

def main():
    pygame.init()  
    X = 1200
    Y = 600
    pos_x = 0
    pos_x_2 = 0 
    pos_x_3 = 400
    pos_y_3 = 400
    display_surface = pygame.display.set_mode((X, Y )) 
    pygame.display.set_caption('Le Rêve de Robotnik ') 
    bg_fix = pygame.image.load('./resources/background_fix.png')
    bg_front = pygame.image.load('./resources/background_front.png')
    bg_middle = pygame.image.load('./resources/background_middle.png')
    sonic = pygame.image.load('./resources/sonic.png')
    rect = pygame.Rect(1050,0,175,175)

    while True :
        keys_pressed = pygame.key.get_pressed()
        display_surface.blit(bg_fix, (0, 0))
        parallaxe(display_surface,bg_middle,pos_x,30)
        parallaxe(display_surface,bg_middle,pos_x -1200, 0)
        display_surface.blit(sonic,(pos_x_3,pos_y_3),rect)
        parallaxe(display_surface,bg_front,pos_x_2,80)
        parallaxe(display_surface,bg_front,pos_x_2 -1200,0) 
        pygame.display.update()
        pos_x += 1
        pos_x_2 += 5
        if pos_x >= 1200 :
            pos_x = 0
        if pos_x_2 >= 1200 :
            pos_x_2 = 0

        if keys_pressed[pygame.K_RIGHT]:
            pos_x_3 += 20
            rect.left = 175
            rect.top = 175
            display_surface.blit(sonic,(pos_x_3,pos_y_3),rect)
            if pos_x_3 >= 1200 :
                pos_x_3 = -100
        else :
            rect.left = 175
        if keys_pressed[pygame.K_LEFT]:
            pos_x_3 -= 20
            rect.left = 175
            rect.top = 175
            display_surface.blit(sonic,(pos_x_3,pos_y_3),rect)
            if pos_x_3 <= -100 :
                pos_x_3 = 1200
        elif keys_pressed[pygame.K_SPACE]:
           pos_y_3 -= 20
           rect.top = 700
           rect.left = 175
        else: 
            rect.top = 0
            rect.left = 1050
            while pos_y_3 < 400 :
                pos_y_3 += 1
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                pygame.quit() 
                quit() 
    pygame.display.flip()
    return

if __name__ == "__main__":
    main()