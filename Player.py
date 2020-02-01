class Player:
	def __init__(self, number):
		self.pos = [370, 480]
		self.vel = 0

		if (number == 1):
			print("recycling bin")
		elif (number == 2):
			print("trash bin")

	def update(self, dt):
		print(self.vel)
		self.pos[0] += self.vel * dt

		if (self.pos[0] < -50):
			self.pos[0] = -50
			self.vel = 0
		elif (self.pos[0] > 720):
			self.pos[0] = 720
			self.vel = 0

		if (self.vel > 0):
			self.vel -= dt * 0.0001
		if (self.vel < 0):
			self.vel += dt * 0.0001

	def thrustLeft(self, dt):
		self.vel -= dt * 0.001

	def thrustRight(self, dt):
		self.vel += dt * 0.001
