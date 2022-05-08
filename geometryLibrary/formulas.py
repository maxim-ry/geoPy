class coordinatePair:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
	def distanceFormula(x1, y1, x2, y2):
		answer = round((((x2 - x1)**2) + ((y2-y1)**2))**0.5, 2)
		return answer
	def slopeFormula(x1, y1, x2, y2):
		answer = (y2 - y1)/(x2 - x1)
		return answer
	def yIntFormula(x1, y1, x2, y2):
		slope = (y2 - y1)/(x2 - x1)
		answer = int(y1 - slope * x1)
		return answer

class pythagoreanTheorem:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def hypotenuse(a, b):
		answer = round(((a**2) + (b**2))**0.5, 2)
		return answer

class interiorAnglesFormula:
	def __init__(self, sides):
		self.sides = sides
	def sumOfInteriorAngles(sides):
		answer = (sides - 2) * 180
		return answer
	def interiorAngle(sides):
		answer = ((sides - 2) * 180) / sides
		return answer