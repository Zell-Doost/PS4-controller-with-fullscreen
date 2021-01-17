import pygame
import os
import sys

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("game")
button = False

font = pygame.font.Font("freesansbold.ttf", 32)
button_down = False

def drawText(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

clock = pygame.time.Clock()
#     controller init
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
                
        if event.type == pygame.JOYBUTTONDOWN:
            button_down = True
        if event.type == pygame.JOYBUTTONUP:
            button_down = False
            
    if button_down:
        drawText("button down", font, (255, 255, 255), screen, 100, 100)
    elif not button_down:
        drawText("button up", font, (255, 255, 255), screen, 100, 100)
                    
    
    
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(45)
                    
                    