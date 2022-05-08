import geometryLibrary.formulaFunctions as forfun

def menu():
	choice = input("""
====================================================================
1 - Find Length Of Plotted Line [Distance Formula]
2 - Find Hypotenuse [Pythagorean Theorem]
3 - Find Slope And Y-Intercept [Slope Intercept Formula]
4 - Find Sum Of Interior Angles [Interior Angle Formula]
5 - Find Size Of Each Interior Angle [Interior Angle Formula]

Type "q" To Exit
====================================================================
Please Type The Number Of Your Choice: """)

	if choice == '1':
		print("")
		forfun.calculateDistance()
		menu()
	elif choice == '2':
		print("")
		forfun.calculateHypotenuse()
		menu()
	elif choice == '3':
		print("")
		forfun.calculateSlope()
		menu()
	elif choice == '4':
		print("")
		forfun.calculateSumOfInteriorAngles()
		menu()
	elif choice == '5':
		print("")
		forfun.calculateInteriorAngle()
		menu()
	elif choice == 'q':
		print('')
		print('Exiting...')
		pass
	else:
		print('')
		print('Invalid Answer')
		menu()

menu()