# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank =pd.read_csv(path)
#print(bank)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(exclude='object')
print(numerical_var)
# code starts here






# code ends here


# --------------
# code starts here

banks=bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())

bank_mode=banks.mode()
print(bank_mode)

#banks=banks.fillna(banks.mode())
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
#print(banks)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here


avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values=['LoanAmount'])
print(avg_loan_amount)
# code ends here



# --------------
# code starts here


loan_approved_se=len(banks[(banks['Self_Employed']=='Yes') &(banks['Loan_Status']=='Y')]) 
loan_approved_nse=len(banks[(banks['Self_Employed']=='No') &(banks['Loan_Status']=='Y')])
Loan_Status=614

percentage_se=loan_approved_se*100/Loan_Status
percentage_nse=loan_approved_nse*100/Loan_Status
print(percentage_nse)
print(percentage_se)
# code ends here


# --------------
# code starts here


loan_term=banks['Loan_Amount_Term'].apply(lambda x : x/12)
print(len(loan_term))
big_loan_term=(sum(list(loan_term>=25)))
print(big_loan_term)
# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
mean_values=loan_groupby.agg([np.mean])
print(loan_groupby)
print(mean_values)
# code ends here


