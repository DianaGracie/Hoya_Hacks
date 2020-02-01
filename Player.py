class Player:
	def __init__(self, number):
		self.vel = [0, 0.02]
		self.flag = 1

		if (number == 1):
			self.pos = [370, 470]
		elif (number == 2):
			self.pos = [370, 490]

	def update(self, dt):
		self.pos[0] += self.vel[0] * dt
		self.pos[1] += self.vel[1] * dt * self.flag

		if (self.pos[1] > 490):
			self.flag *= -1
			self.pos[1] = 490
		elif (self.pos[1] < 470):
			self.flag *= -1
			self.pos[1] = 470

		if (self.pos[0] < -50):
			self.pos[0] = -50
			self.vel[0] = 0
		elif (self.pos[0] > 720):
			self.pos[0] = 720
			self.vel[0] = 0


		if (self.vel[0] > 0):
			self.vel[0] -= dt * 0.0001
		if (self.vel[0] < 0):
			self.vel[0] += dt * 0.0001

		if (self.vel[1] > 0.025):
			self.vel[1] = 0.025
		if (self.vel[1] < 0.02):
			self.vel[1] = 0.02
		else:
			self.vel[1] -= 0.0001 * dt


	def thrustLeft(self, dt):
		self.vel[0] -= dt * 0.001
		self.vel[1] += dt * 0.001

	def thrustRight(self, dt):
		self.vel[0] += dt * 0.001
		self.vel[1] += dt * 0.001
