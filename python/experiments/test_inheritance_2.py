
class Shape:
	def __init__(self, color, name):
		self.color = color
		self.name = name

	def print_info(self):
		print("type: %s, color: %s" % (self.name, self.color))


class Line(Shape):
	def __init__(self, color, start_x, start_y, end_x, end_y):
		Shape.__init__(self, color, "line")
		self.start_x = start_x
		self.start_y = start_y
		self.end_x = end_x
		self.end_y = end_y


class Cirlce(Shape):
	def __init__(self, color, start_x, start_y):
		Shape.__init__(self, color, "circle")
		self.start_x = start_x
		self.start_y = start_y

line = Line("red", 0, 0, 10, 10)
circle = Cirlce("green", 5, 5)

shapes_list = [line, circle]

for shape in shapes_list:
	shape.print_info()
