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

    def processInput(self, window, logic, dt):
        pressed = pygame.key.get_pressed()

        if (logic.state == "endgame"):
            pass

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
                pass

    def draw(self, window, logic):
        if (logic.state == "endgame"):
            window.fill((255, 0, 0))
        if (logic.state == "playing"):
            # RGB = Red, Green, Blue
            window.fill((0, 0, 0))
            # Background Image
            if (logic.bg_state):
                window.blit(self.bg1, (0, 0))
            else:
                window.blit(self.bg2, (0, 0))

            #draw trash
            for trash in logic.trash_list:
                if (trash.id > 5):
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
                sfx = 'music/Splash' + str(randint(1,3)) + '.wav'
                effect = pygame.mixer.Sound(sfx)
                print(sfx)
                effect.play()
                logic.miss = 0

            if logic.wrong:
                effect = pygame.mixer.Sound('music/laser.wav')
                effect.play()
                logic.wrong = 0

            #pygame.draw.rect(window, (0,0,0), (logic.p1.pos[0], trash.pos[1], ))
        
        pygame.display.update()