
import numpy 
import matplotlib.pyplot as plt 
import scipy.integrate

filename = "droptower_vdata.txt"


def main():
	dataArr = numpy.loadtxt(filename) #ONLY loads float numbers from a file

	tVals = []
	vyVals = []

	for i in range(0, len(dataArr)):
		t = dataArr[i][0]
		tVals.append(t)
		vy = dataArr[i][1]
		vyVals.append(vy)


	#print(dataArr)
	#print(tVals)
	#print(vyVals)

	accelerations = differentiate(tVals, vyVals)
	print (accelerations)

	positions = integrate(vyVals)
	print(positions)

	plt.plot(tVals, positions)
	plt.show()

	plt.plot(tVals, vyVals)

	plt.show()

	plt.plot(tVals[:-1], accelerations) 
	#the first argument of plt.plot takes the elements of the array fromt the first to the n-1th element

	plt.show()

	avgUpAcc = giveUpwardAcc(accelerations)
	print("Average upward acceleration = ", numpy.sum(avgUpAcc)/len(avgUpAcc))

def differentiate(xs, ys):
	diffYs = numpy.diff(ys)
	diffXs = numpy.diff(xs)

	diffs = diffYs / diffXs
	return diffs

def integrate(ys):
	integrals = scipy.integrate.cumtrapz(ys, dx = 1.0, initial = 0)
	return integrals

def giveUpwardAcc(accs):
	upAcc = []
	for i in range(0, len(accs)):
		if accs[i] > 0:
			upAcc.append(accs[i])
	return numpy.array(upAcc)

main()	

