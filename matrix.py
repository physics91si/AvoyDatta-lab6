
import numpy as np
import matplotlib.pyplot as plt 

def main():

	arrZeros = np.zeros((9, 9))
	for  i in range(0, len(arrZeros)):
		for j in range(0, 3):
			arrZeros[i][j] = 1

	for i in range(0, len(arrZeros[0])):
		arrZeros[len(arrZeros) - 1][i] = 1

	arrZeros[(4, 7, 1),(5, 7, 8)] = 1 #Sets arrZeros[x's, y's] to the value of the RHS. x's and y's have been entered as tuples
	print(arrZeros)
	plt.spy(arrZeros)
	plt.show()

main()
