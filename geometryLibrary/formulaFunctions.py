import geometryLibrary.formulas as formulas
from fractions import Fraction
	
def calculateDistance():
	x1 = int(input("Type x1: "))
	y1 = int(input("Type y1: "))
	x2 = int(input("Type x2: "))
	y2 = int(input("Type y2: "))

	orderPairs = ' [' + str(x1) + ', ' + str(y1) + '] And [' + str(x2) + ', ' + str(y2) + ']'

	print('')
	print('====================================================================')
	print('You Will Be Using' + orderPairs)
	print('''
		Calculating...
	''')

	answer = str(formulas.coordinatePair.distanceFormula(x1, y1, x2, y2))
	print('The Length Of The Line Is ' + answer)

	print('====================================================================')

def calculateHypotenuse():
	a = int(input("Type side A: "))
	b = int(input("Type side B: "))

	sides = 'Side A Is Equal To ' + str(a) + ' And Side B Is Equal To ' + str(b)

	print('')
	print('====================================================================')
	print(sides)
	print('''
		Calculating...
	''')

	answer = str(formulas.pythagoreanTheorem.hypotenuse(a, b))
	print('The Length Of The Hypotenuse Is ' + answer)

	print('====================================================================')


def calculateSlope():
	x1 = int(input("Type x1: "))
	y1 = int(input("Type y1: "))
	x2 = int(input("Type x2: "))
	y2 = int(input("Type y2: "))

	orderPairs = ' [' + str(x1) + ', ' + str(y1) + '] And [' + str(x2) + ', ' + str(y2) + ']'

	print('')
	print('====================================================================')
	print('You Will Be Using' + orderPairs)
	print('''
		Calculating...
	''')




	# slope = str(Fraction(formulas.coordinatePair.slopeFormula(x1, y1, x2, y2)))
	slope = str(Fraction(formulas.coordinatePair.slopeFormula(x1, y1, x2, y2)).limit_denominator(1000))
	yInt = str(formulas.coordinatePair.yIntFormula(x1, y1, x2, y2))
	print('The Slope Is ' + slope + ' And The Y-Intercept Is ' + yInt)
	print('The Slope Intercept Formula Is: y = ' + slope + 'x + ' + yInt)

	print('====================================================================')

def calculateSumOfInteriorAngles():
	sides = int(input("Type Amount Of Sides: "))

	print('')
	print('====================================================================')
	print('Your Polygon Will Have ' + str(sides) + ' Sides')
	print('''
		Calculating...
	''')

	answer = str(formulas.interiorAnglesFormula.sumOfInteriorAngles(sides))
	print('The Sum Of The Interior Angles Is ' + answer + ' Degrees')

	print('====================================================================')

def calculateInteriorAngle():
	sides = int(input("Type Amount Of Sides: "))

	print('')
	print('====================================================================')
	print('Your Polygon Will Have ' + str(sides) + ' Sides')
	print('''
		Calculating...
	''')

	answer = str(formulas.interiorAnglesFormula.interiorAngle(sides))
	print('Each Angle Of The Polygon Is ' + answer + ' Degrees')

	print('====================================================================')