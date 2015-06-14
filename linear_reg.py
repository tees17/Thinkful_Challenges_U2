import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']
# loanleng = loansData['Loan.Length']


#remove % symbol from interest rate and convert to float
intrate = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]


# # #remove "month" at the end of loan length and convert to integer
# loanleng = [int(length[0:-7]) for length in loansData['Loan.Length']]

# # #create a new column called Fico Score with lower limit value
fico = [int(val.split('-')[0]) for val in loansData['FICO.Range']]

# # The dependent variable
y = np.matrix(intrate).transpose()
# # The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print f.summary()