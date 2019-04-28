from graphics import *
			
class gate:
	def __init__(self, output = False, pos = Point(0,0)):
		self.inputs = []
		self.output = output
		self.img = Circle(pos,10)
	
	def update_output(self):
		self.update_color()
		
	def update_color(self):
		if (self.output):
			self.img.setFill("green")
		else:
			self.img.setFill("red")
		
class and_gate(gate):
	def __init__(self, output = False, pos = Point(0,0)):
		gate.__init__(self, output, pos)
	
	def update_output(self):
		if (not self.inputs): #empty list
			self.output = False
		else:
			self.output = True
			for i in self.inputs:
				if (not i.output):
					self.output = False
					break
		super().update_color()
		
	
class or_gate(gate):
	def __init__(self, output = False, pos = Point(0,0)):
		gate.__init__(self, output, pos)
	
	def update_output(self):
		if (not self.inputs): #empty list
			self.output = False
		else:
			self.output = False
			for i in self.inputs:
				if (i.output):
					self.output = True
					break
		super().update_color()

def main():
	gates = []
	win = GraphWin("Circuit", 400, 400)

	key = None
	while(key != 'x'):
		key = win.checkKey()
		pos = win.checkMouse()
		if pos is not None:
			gates.append(and_gate(pos = pos))
			gates[len(gates)-1].img.draw(win)
		if (key == 'r'):
			for g in gates:
				g.update_output()

if __name__ == "__main__":
	main()