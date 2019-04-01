from CL import Dog
class BullDog(Dog):
	def __init__(self, N, A, W):
		Dog.__init__(self, '@', A)
		self.weight = W
	def Sleep(self):
		self.energy += 50
		print(self.energy)
	def Move(self):
		for i in  
		self.body[0] = 

class Alabay(Dog):
	def __init__(self, N, A, P):
		BullDog.__init__(self, '#', A)
		self.power = P
	def Attack(self):
		self.energy -= 50
		print(self.energy)
def main():
	b = BullDog("Richy", 20, 40)
	print(b.weight, b.name, b.age)
	b.run()
	print(b.golos())
	b.Sleep()
	t = Alabay("Aktos", 25, 1000)
	t.Attack()
	t.name = "Kask"
	print(t.name)

main()
