import scipy.stats as stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# Performs chi squared test and prints the result
chi, p = stats.chisquare(freq.values())
print chi
print p

# plt.figure()
# plt.bar(freq.keys(), freq.values(), width=1)
# plt.show()