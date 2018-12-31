# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
p_a=((df['fico']>700).sum())/len(df)
print(p_a)
p_b=((df['purpose']=='debt_consolidation').sum())/len(df)
print(p_b)
df1=df[df['purpose']=='debt_consolidation']
p_a_b=(((df['purpose']=='debt_consolidation') &(df['fico']>700)).sum())/len(df)
print(p_a_b)
pAoverB=(p_a*p_a_b)/p_b
result=False
if pAoverB==p_a:
    result=True
print(result)
# code ends here


# --------------
# code starts here
prob_lp=((df['paid.back.loan']=='Yes').sum())/len(df)
print(prob_lp)
prob_cs=((df['credit.policy']=='Yes').sum())/len(df)
print(prob_cs)
new_df=df[df['paid.back.loan']=='Yes']
prob_pd_cs=((new_df['credit.policy']=='Yes').sum())/len(new_df)
print(prob_pd_cs)
bayes=(prob_lp*prob_pd_cs)/(prob_cs)
print(bayes)

# code ends here


# --------------
# code starts here
q=df['purpose']
q.value_counts(normalize=True).plot(kind='bar')
df1=df[df['paid.back.loan']=='No']
df1['purpose'].value_counts(normalize=True).plot(kind='bar')
plt.show()
# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
df['installment'].hist(bins=10)
df['log.annual.inc'].hist(bins=10)


# code ends here


