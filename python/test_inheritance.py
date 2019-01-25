class Figure:
	"""docstring for Figure"""
	def __init__(self, color):
		self.color = color
	def get_color(self):
		return self.color
	def get_info(self):
		print("Figure")
		print("Color: " + self.color)


class Rectangle(Figure):
	"""docstring for Rectangle(Figure)"""
	def __init__(self, color, width=100, height=100):
		super().__init__(color)
		self.width=width
		self.height=height
	def square(self):
		return self.width * self.height
	
	def get_info(self):
		print("Rectangle")
		print("width, height =", self.width, self.height)


f1 = Figure("red")
f1.get_info()

rec1 = Rectangle("blue")
rec1.get_info()

rec2 = Rectangle("red", 25, 10)
rec2.get_info()
