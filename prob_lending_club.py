# Write a script called "prob_lending_club.py" that reads in the loan data, cleans it, and loads it into a pandas DataFrame. 
# Use the script to generate and save a boxplot, histogram, and QQ-plot for the values in the "Amount.Requested" column. 

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

plt.figure()
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

loansData.boxplot(column='Amount.Requested')
plt.show()

plt.figure()
loansData.hist(column='Amount.Requested')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()