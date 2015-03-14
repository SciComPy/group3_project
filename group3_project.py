import random
import pylab
 
#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5
#set font size for text
pylab.rcParams['legend.fontsize'] = 20


class MonteCarloSimulationOfPi():

	#calculate the standard deviation
	def stdDev(self,X):
		mean = sum(X)/float(len(X))
		total = 0.0
		for x in X:
			total += (x - mean)**2
		return (total/len(X))**0.5

	def throwNeedles(self,numNeedles):
		assert numNeedles > 1, "The Number of needles must be greater than 1"
        	assert numNeedles == int(numNeedles), "The Number of needles must be an integer"
		inCircle = 0
		for Needles in xrange(1, numNeedles + 1, 1):
			x = random.random()
			y = random.random()
			if (x*x + y*y)**0.5 <= 1.0:
				inCircle += 1
		return 4*(inCircle/float(numNeedles))

	def getEst(self,numNeedles, numTrials):
		assert numNeedles > 1, "Number of needles must be greater than 1"
        	assert numNeedles == int(numNeedles), "Number of needles must be an integer"
        	assert numTrials > 0, "Number of trials must be greater than 0"
        	assert numTrials == int(numTrials), "Number of trials must be an integer"
		estimates = []
		for t in range(numTrials):
			piGuess = self.throwNeedles(numNeedles)
			estimates.append(piGuess)
		sDev = self.stdDev(estimates)
		curEst = sum(estimates)/len(estimates)
		print 'Est. = ' + str(curEst) +\
			  ', Std. dev. = ' + str(round(sDev, 6))\
			  + ', Needles = ' + str(numNeedles)
		return (curEst, sDev)

	def estPi(self,precision, numTrials):
		assert precision > 0, "The Precision value must be greater than 0"
        	assert numTrials > 0, "The Number of trials must be greater than 0"
        	assert numTrials == int(numTrials), "The Number of trials must be an integer"
		numNeedles = 1000
		sDev = precision
		while sDev >= precision/2.0:
			curEst, sDev = self.getEst(numNeedles, numTrials)
			numNeedles *= 2
		return curEst

def main():
    
    simulate = MonteCarloSimulationOfPi()
    simulate.estPi(0.005, 100)

if __name__ == '__main__':
    main()		

