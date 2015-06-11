
import collections
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

test_data = [1, 4, 5, 6, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#outputs the frequencies of test_data
c = collections.Counter(test_data)
count_sum = sum(c.values())
for k,v in c.iteritems():
	print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

# creates and saves a boxplot
plt.boxplot(test_data)
plt.savefig("test_dataBoxPlot.png")

# creates and saves a histogram
plt.figure()
plt.hist(test_data, histtype='bar')
plt.savefig("test_dataHisto.png")

# creates and saves QQ-plot 
plt.figure()
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("test_dataQQ.png") 
