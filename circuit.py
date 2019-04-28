from graphics import *
			
class gate:
	def __init__(self, output = False, pos = Point(0,0)):
		self.inputs = []
		self.output = output
		self.img = Circle(pos,10)
		self.text = Text(pos, "G")
	
	def update_output(self):
		self.update_color()
		
	def update_color(self):
		if (self.output):
			self.img.setFill("green")
		else:
			self.img.setFill("red")
			
	def draw_self(self, win):
		self.img.draw(win)
		self.text.draw(win)
		
class and_gate(gate):
	def __init__(self, output = False, pos = Point(0,0)):
		gate.__init__(self, output, pos)
		self.text = Text(pos, "A")
	
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
		self.text = Text(pos, "O")
	
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
	most_recent_key = 'z'
	while(key != 'x'):
		key = win.checkKey()
		if (key != ""):
			most_recent_key = key
		
		pos = win.checkMouse()
		if pos is not None:
			if (most_recent_key == 'a'):
				gate_type = and_gate
			elif (most_recent_key == 's'):
				gate_type = or_gate
			else:
				gate_type = gate
			
			gates.append(gate_type(pos = pos))
			gates[len(gates)-1].draw_self(win)
		if (key == 'r'):
			for g in gates:
				g.update_output()

if __name__ == "__main__":
	main()