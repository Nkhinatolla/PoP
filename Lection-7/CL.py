class Dog:
	energy = 100
	def __init__(self, s, A):
		self.sign = s
		self.age = A
	def run(self):
		self.energy -= 10
		print("Running...",self.energy)
	
	def golos(self):
		return (self.name + " is gaffing")

def main():
	sally = Dog("Sally", 4)
	milly = Dog("Milly", 12)
	milly.run()
	sally.run()

	print(sally.golos())
	print(sally.name,sally.age)
	invalid("Name", 23, )

# main()
