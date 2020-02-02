from Player import Player
from Trash import Trash
from random import * 

class GameLogic:
	def __init__(self):
		self.state = "playing"
		self.p1 = Player(1)
		self.p2 = Player(2)
		self.trash_list = []
		self.bg_state = True
		self.switch_counter = 0
		self.trash_timer = 0
		self.pollution = 0
		self.correctcapture = 0
		self.miss = 0
		self.wrong = 0

	def update(self, dt):
		self.p1.update(dt)
		self.p2.update(dt)
		#have trash fall
		for trash in self.trash_list:
			trash.update(dt)

		#switch background
		self.switch_counter += dt * 0.1
		if (self.switch_counter >= 40):
			self.bg_state = not self.bg_state
			self.switch_counter = 0

		#generate trash
		self.trash_timer += dt * 0.1
		if (self.trash_timer >= 200*random()+100):
			self.trash_timer = 0
			self.trash_list.append(Trash())

		#detect collisions
		for trash in self.trash_list:
			if (trash.pos[1] > 420):

				if (self.p1.pos[0] < trash.pos[0]*800 and self.p1.pos[0] + 50 > trash.pos[0]*800):
					if trash.isTrash == True:
						self.correctcapture = 1
						self.trash_list.remove(trash)
					else:
						self.wrong = 1
						self.trash_list.remove(trash)
				
				if (self.p2.pos[0] < trash.pos[0]*800 and self.p2.pos[0] + 50 > trash.pos[0]*800):
					if trash.isTrash == False:
						self.correctcapture = 1
						self.trash_list.remove(trash)
					else:
						self.wrong = 1
						self.trash_list.remove(trash)

				elif (trash.pos[1] > 540):
					#handle trash water collision
					self.trash_list.remove(trash)
					self.miss = 1
					self.pollution += 5
					#check endgame
					if (self.pollution >= 100):
						self.state = "endgame"

