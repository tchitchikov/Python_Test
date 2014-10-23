"""
__author__ john
The goal of this application is to calculate Standard Deviation.
1) get a total count	(n)
2) find the mean 		(x bar)
3) subtract each instance (x sub i) from the mean (x bar)
4) square each result of instance minus mean
5) sum the total of squares
6) divide by the total count minus 1 (n-1)
7) take the square root of the result

sqrt(sum((xSubI - xBar)^2)/(n-1))

"""

data = [1, 3, 4, 5, 5, 5, 8, 15, 16, 19, 21]

class Stat:
	def variance(data):
		#sum((xSubI - xBar)^2)/(n-1)
		n = 0
		xBar = 0.0
		sum = 0.0
		sumDistanceFromMean = 0.0
		distanceFromMean = 0.0
		variance = 0.0
		standardDeviation = 0.0
		listDistanceFromMean = []
		
		
		print("The given set is: {0}".format(data))				
		# get the total count
		n = len(data)
		print("The list is length {0}".format(n))

		# find the mean
		for number in data:
			sum = sum + number
		xBar = sum/n
		print("The mean of the list is {0}".format(xBar))

		# subtract each instance of xSubI from the mean xBar
		for number in data:
			distanceFromMean = number - xBar
			distanceFromMean = distanceFromMean**2
			listDistanceFromMean.append(distanceFromMean)

		# sum the total of squares and divide by n-1
		for number in listDistanceFromMean:
			sumDistanceFromMean = sumDistanceFromMean + number
		varianceValue = sumDistanceFromMean/(n-1)

		# finally take the square root to get the Standard Deviation
		#standardDeviation = variance**0.5
		print("The variance for the given set is {0}".format(varianceValue))
		return varianceValue
		
		
	def standard_deviation(variance, data):
		standardDeviation = variance(data)**0.5
		print("The standard deviation for the given set is {0}".format(standardDeviation))
		# Call the function with from Stat import *
		# data = [ <some set> ]
		# Stat.standard_deviation(Stat.variance, data)
	
