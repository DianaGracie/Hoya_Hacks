import math
import random
import pygame
from pygame import mixer

from GameLogic import GameLogic
from CameraView import CameraView

# Intialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))

# Sound
mixer.music.load("music/background!.wav")
mixer.music.play(-1)
# Caption and Icon
pygame.display.set_caption("Recycle Game")
pygame.display.set_icon(pygame.image.load('images/recycle_bin.png'))

logic = GameLogic()
view = CameraView()
clock = pygame.time.Clock()

#create pollution score
pygame.display.set_caption('Pollution = ' + str(logic.pollution))
red = (255,0,0)

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

# Game Loop
while logic.state != "exit":

    #get elapsed time
    dt = clock.tick(60)
    #process user input
    view.processInput(screen, logic, dt)
    #tick natural game logic
    logic.update(dt)
    #draw window
    view.draw(screen, logic)