# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
print(loan_status)

loan_status.plot(kind='bar')
plt.show()
#Code starts here


# --------------
#Code starts here

property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False,rot=45)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
#plt.xticks(rot=45)
plt.show()


# --------------
#Code starts here
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,rot=45)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.show()



# --------------
#Code starts here

graduate=data[data['Education']=='Graduate']
#print(type(graduate))
not_graduate=data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')












#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(15,20))
x=data['ApplicantIncome']
y=data['LoanAmount']
z=data['CoapplicantIncome']
ax_1.scatter(x,y)
ax_1.set_title("Applicant Income")
ax_2.scatter(z,y)
ax_1.set_title("CoapplicantIncome")
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
p=data['TotalIncome']
ax_3.scatter(p,y)
ax_1.set_title("Total Income")




