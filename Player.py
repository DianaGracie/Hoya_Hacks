class Player:
	def __init__(self, number):
		self.pos = [370, 480]

		if (number == 1):
			print("recycling bin")
		elif (number == 2):
			print("trash bin")

	def update(self, dt):
		pass

	def thrustLeft(self, dt):
		self.pos[0] -= dt

	def thrustRight(self, dt):
		self.pos[0] += dt
