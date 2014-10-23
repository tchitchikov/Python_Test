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

sqrt(sum((x sub i - x bar)^2)/(n-1))

"""

listOfNumbers = [1, 3, 4, 5, 5, 5, 8, 15, 16, 19, 21]
print("The given set is: {0}".format(listOfNumbers))
# get the total count
n = len(listOfNumbers)
print("The list is length {0}".format(n))

# find the mean
sum = 0.0
for number in listOfNumbers:
	sum = sum + number
xBar = sum/n
print("The mean of the list is {0}".format(xBar))

# subtract each instance of xSubI from the mean xBar
listDistanceFromMean = []
for number in listOfNumbers:
	distanceFromMean = number - xBar
	distanceFromMean = distanceFromMean**2
	listDistanceFromMean.append(distanceFromMean)

# sum the total of squares and divide by n-1
sumDistanceFromMean = 0.0
for number in listDistanceFromMean:
	sumDistanceFromMean = sumDistanceFromMean + number
variance = sumDistanceFromMean/(n-1)

# finally take the square root to get the Standard Deviation
standardDeviation = variance**0.5
print("The standard deviation for the given set is {0}".format(standardDeviation))
print("The variance for the given set is {0}".format(variance))