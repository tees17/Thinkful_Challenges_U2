import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('LoanStats3c.csv', usecols= ['home_ownership', 'annual_inc', 'int_rate'])


#Use income (annual_inc) to model interest rates (int_rate)

own = loansData['home_ownership']
own = [2 if x == 'OWN' else 2 if x == 'MORTGAGE' else 1 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in own]
income=loansData['annual_inc']
rate=loansData['int_rate']
income[np.isnan(income)]=0
rate[np.isnan(rate)]=0


# The dependent variable
y = np.matrix(rate).transpose()

#the independent variables
x1=np.matrix(income).transpose()
x2=np.matrix(own).transpose()


x=np.column_stack([x1,x2])
X=sm.add_constant(x)


model = sm.OLS(y,X)
f = model.fit()
print f.summary()
