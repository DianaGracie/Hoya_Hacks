import pygame
from random import *

class CameraView:
    def __init__(self):
        self.player_image_1 = pygame.image.load('images/trash.png')
        self.player_image_2 = pygame.image.load('images/recycle_bin.png')
        self.bg1 = pygame.image.load('images/background.png')
        self.bg2 = pygame.image.load('images/background2.png')

        self.garbage = [pygame.image.load('images/garbage/1.png'),
            pygame.image.load('images/garbage/2.png'), 
            pygame.image.load('images/garbage/3.png'),
            pygame.image.load('images/garbage/4.png'),
            pygame.image.load('images/garbage/5.png'),
            pygame.image.load('images/garbage/6.png'),
            pygame.image.load('images/garbage/7.png')]

        self.recycle = [pygame.image.load('images/recyclables/1.png'),
            pygame.image.load('images/recyclables/2.png'),
            pygame.image.load('images/recyclables/3.png'),
            pygame.image.load('images/recyclables/4.png'),
            pygame.image.load('images/recyclables/5.png'),
            pygame.image.load('images/recyclables/6.png'),
            pygame.image.load('images/recyclables/7.png')]


    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def processInput(self, window, logic, dt):
        pressed = pygame.key.get_pressed()

        if (logic.state == "endgame"):
            if (pressed[pygame.K_RETURN]):
                logic.pollution = 0
                logic.trash_list.clear()
                logic.state = "playing"

        if (logic.state == "playing"):
            if (pressed[pygame.K_LEFT]):
                logic.p1.thrustLeft(dt)
            if (pressed[pygame.K_RIGHT]):
                logic.p1.thrustRight(dt)

            if (pressed[pygame.K_a]):
                logic.p2.thrustLeft(dt)
            if (pressed[pygame.K_d]):
                logic.p2.thrustRight(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logic.state = "exit"
                
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (logic.state == "paused"):
                        logic.state = "playing"
                    elif (logic.state == "playing"):
                        logic.state = "paused"

    def draw(self, window, logic):
        if (logic.state == "endgame"):
            window.fill((255, 0, 0))
            largeText = pygame.font.Font('freesansbold.ttf', 50)
            TextSurf, TextRect = self.text_objects("Pollution = " + str(logic.pollution) + "%", largeText, (0,0,0))
            TextRect.center = ((800/2),(600/2))
            window.blit(TextSurf, TextRect)
            TextSurf, TextRect = self.text_objects("Press Enter to Try Again", largeText, (0,0,0))
            TextRect.center = ((800/2),(600/4))
            window.blit(TextSurf, TextRect)

        if (logic.state == "playing" or logic.state == "paused"):
            # RGB = Red, Green, Blue
            window.fill((0, 0, 0))
            # Background Image
            if (logic.bg_state):
                window.blit(self.bg1, (0, 0))
            else:
                window.blit(self.bg2, (0, 0))

            #draw trash
            for trash in logic.trash_list:
                if (trash.id > 7):
                    trash_pic = self.recycle[trash.id - 8]
                    trash.isTrash = False
                else:
                    trash_pic = self.garbage[trash.id - 1]
                window.blit(trash_pic, (trash.pos[0]*800, trash.pos[1]))
     
            #draw player bins
            window.blit(self.player_image_1,(logic.p1.pos[0], logic.p1.pos[1]))
            window.blit(self.player_image_2,(logic.p2.pos[0], logic.p2.pos[1]))

            #play the sound
            if logic.correctcapture:
                effect = pygame.mixer.Sound('music/SmallSuccess.wav')
                effect.play()
                logic.correctcapture = 0

            if logic.miss:
                effect = pygame.mixer.Sound('music/Splash' + str(randint(1,3)) + '.wav')
                effect.play()
                logic.miss = 0

            if logic.wrong:
                effect = pygame.mixer.Sound('music/laser.wav')
                effect.play()
                logic.wrong = 0

            largeText = pygame.font.Font('freesansbold.ttf', 30)
            TextSurf, TextRect = self.text_objects("Pollution = " + str(logic.pollution) + "%", largeText, (255,0,0))
            TextRect.center = ((800/5),(600/8.5))
            window.blit(TextSurf, TextRect)

            if (logic.state == "paused"):
                s = pygame.Surface((800, 600))
                s.set_alpha(120)
                s.fill((255,255, 0))
                window.blit(s, (0,0))
        
        pygame.display.update()