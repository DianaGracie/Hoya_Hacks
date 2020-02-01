import pygame

class CameraView:
    def __init__(self):
        self.player_image_1 = pygame.image.load('images/trash.png')
        self.player_image_2 = pygame.image.load('images/recycle_bin.png')
        self.trash_image = pygame.image.load('images/enemy.png')
        self.background_image = pygame.image.load('images/background.png')

    def processInput(self, window, logic, dt):
        pressed = pygame.key.get_pressed()

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
        # RGB = Red, Green, Blue
        window.fill((0, 0, 0))
        # Background Image
        window.blit(self.background_image, (0, 0))
 
        window.blit(self.player_image_1,(logic.p1.pos[0], logic.p1.pos[1]))
        window.blit(self.player_image_2,(logic.p2.pos[0], logic.p2.pos[1]))
        for trash in logic.trash_list:
            window.blit(self.trash_image,(trash.pos[0], trash.pos[1]))
        pygame.display.update()