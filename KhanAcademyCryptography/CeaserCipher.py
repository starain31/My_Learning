
from __future__ import print_function

def printGraph(frequency):
	max_freq = max(frequency)
	while 0 <= max_freq:
		for i in range(0, len(frequency)):
			if frequency[i] <= 0:
				print(" = ", end='')
			else:
				print("  ", end='')
			frequency[i] -= 1
		print("\n")
		max_freq -= 1;


frequency = [1, 3, 5, 3, 4, 5, 5, 6, 3, 6, 6, 7]
printGraph(frequency)
