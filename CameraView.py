class CameraView:
	def __init__(self):
		self.player_image_1 = pygame.image.load('images/ufo.png')
		self.player_image_2 = pygame.image.load('images/ufo.png')
		self.trash_image = pygame.image.load('images/enemy.png')

	def processInput(self, window, logic, dt):
		pass

	def draw(self, window, logic):
		window.blit(self.player_image_1,(logic.p1.pos[0], logic.p1.pos[1]))
		window.blit(self.player_image_2,(logic.p2.pos[0], logic.p2.pos[1]))
		for trash in logic.trash_list:
			window.blit(self.trash_image,(trash.pos[0], trash.pos[1]))

