# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data=pd.read_csv(path)
cols=data.columns
#print(cols)
data['Gender']=data['Gender'].apply(lambda x:x.replace("-",'Agender'))
gender_count=data["Gender"].value_counts()
gender_count.plot(kind='bar')


# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
alignment.plot.pie(label='Character Alignment')


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
#print(sc_df)
covariance=sc_df.cov()
sc_covariance=covariance.values[0,1]
#covariance=covariance[0,1]
#print(covariance)
sc_strength=data['Strength'].std()
sc_combat=data['Combat'].std()
print(sc_combat)
sc_pearson=sc_covariance/(sc_combat*sc_strength)
print(sc_pearson)
ic_df=data[['Intelligence','Combat']]
covariance=ic_df.cov()
ic_covariance=covariance.values[0,1]
#covariance=covariance[0,1]
#print(covariance)
ic_intelligence=data['Intelligence'].std()
ic_combat=data['Combat'].std()
print(ic_combat)
ic_pearson=ic_covariance/(ic_combat*ic_intelligence)
print(ic_pearson)


# --------------
#Code starts here

total_high=data['Total'].quantile(.99)
print(total_high)

super_best=data[data["Total"]>total_high]

super_best_names=list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
#boxplot = super_best.boxplot(column=['Intelligence', 'Speed', 'Power'])
#l=['Intelligence','Speed','Power']
fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3,figsize=(20,10))
#for i,el in enumerate(l):
 #   a = super_best.boxplot('Name', by=el,)
ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Intelligence')
ax_3.boxplot(super_best['Power'])
ax_3.set_title('Intelligence')


