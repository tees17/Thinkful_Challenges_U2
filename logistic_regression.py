import pandas as pd
import statsmodels.api as sm 
import math as math
import matplotlib.pyplot as plt

# Load cleaned data and finish clean-up on FICO range
loansD = pd.read_csv('loansData_clean.csv')
loansD['FICO.Score'] = [int(val.split('-')[0]) for val in loansD['FICO.Range']]

#Add a column to your dataframe indicatng whether the interest rate is < 12%. 
#This would be a derived column that you create from the interest rate column. You name it IR_TF. 
#It would contain binary values, i.e.'0' when interest rate < 12% or '1' when interest rate is >= 12%

IR_TF=loansD['Interest.Rate'].map(lambda x: 1 if x >= .12 else 0)
loansD['IR_TF']=IR_TF 

#Create a new data frame containing only the dependent and indepenent variables of the function
newLoan=loansD.loc[:,['IR_TF','FICO.Score','Amount.Funded.By.Investors']] 
newLoan['Intercept'] = 1.0

#Rename columns
newLoan.columns = ['IR_TF','FICO.Score','Loan.Amount','Intercept']

#define the indepedent variables
ind_vars = newLoan.columns[1:]

#Run the logistic regression model
logit = sm.Logit(newLoan['IR_TF'], newLoan[ind_vars])
result = logit.fit()
print result.summary()
coeff = result.params

#Define a function for prediction
def Logistic_Func( coeff, FICO, Amt):
	lineF = coeff['Intercept'] + coeff['Loan.Amount']*Amt + coeff['FICO.Score']*FICO;
	print lineF;
	e  = math.e
	prob = 1 / (1 + e ** lineF)
	print prob

Logistic_Func (coeff, 720, 10000)


#print loansD[ind_vars].info()