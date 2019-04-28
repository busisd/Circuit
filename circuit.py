from graphics import *
			
class gate:
	def __init__(self, output = False, pos = Point(0,0)):
		self.inputs = []
		self.output = output
		self.radius = 10
		self.pos = pos
		self.img = Circle(pos,self.radius)
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

def dist_between(pos1, pos2):
	return ( (pos1.getX()-pos2.getX())**2 + (pos1.getY()-pos2.getY())**2 )**(1/2)

def find_gate_clicked(pos, gates):
	gate_found = None
	for cur_gate in gates:
		if (dist_between(pos, cur_gate.pos) < cur_gate.radius):
			gate_found = cur_gate
			break
	return gate_found

def main():
	gates = []
	win = GraphWin("Circuit", 400, 400)

	key = None
	most_recent_key = 'z'
	start_gate = None
	while(key != 'x'):
		key = win.checkKey()
		if (key != ""):
			most_recent_key = key
		
		pos = win.checkMouse()
		if pos is not None:
			gate_clicked = find_gate_clicked(pos, gates)
			if (gate_clicked is None):
				if (most_recent_key == 'a'):
					gate_type = and_gate
				elif (most_recent_key == 's'):
					gate_type = or_gate
				elif (most_recent_key == 'd'):
					gate_type = gate
				else:
					gate_type = None
				
				if (gate_type is not None):
					gates.append(gate_type(pos = pos))
					gates[len(gates)-1].draw_self(win)
					
				start_gate = None
			
			if (gate_clicked is not None):
				if (most_recent_key == 'f'):
					gate_clicked.output = not gate_clicked.output
				if (most_recent_key == 'c'):
					if (start_gate is None):
						start_gate = gate_clicked
					else:
						if (gate_clicked != start_gate):
							gate_clicked.inputs.append(start_gate)
							Line(gate_clicked.pos, start_gate.pos).draw(win)
						start_gate = None
				
			for cur_gate in gates:
				cur_gate.update_output()
			
		if (key == 'r'):
			for g in gates:
				g.update_output()

if __name__ == "__main__":
	main()