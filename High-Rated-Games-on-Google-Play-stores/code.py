# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(path)
#data['Rating'].hist()
data=data[data['Rating']<=5]
data['Rating'].hist()
#Code starts here


#Code ends here


# --------------
# code starts here

total_null=pd.Series(data.isnull().sum())
#print(total_null)
# code ends here
percent_null=(total_null/data.isnull().count())
#print(percent_null)
missing_data=pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)

data=data.dropna()
total_null_1=pd.Series(data.isnull().sum())
#print(total_null)
# code ends here
percent_null_1=(total_null_1/data.isnull().count())
#print(percent_null)
missing_data_1=pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)



# --------------
import seaborn as sns

#Code starts here
ax=sns.catplot(x="Category",y="Rating",data=data,height=10,kind='box')
ax.set_titles('Rating vs Category [BoxPlot]')
ax.set_xticklabels(rotation=90)


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import seaborn as sns
#Code starts here
d=data['Installs'].value_counts()
#print(d)
data['Installs']=data['Installs'].apply(lambda x : x.replace(',','')).apply(lambda x : x.replace('+',''))
d=data['Installs'].value_counts()
#print(d)
data['Installs']=data['Installs'].astype(int)
le=LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
y=sns.regplot(data=data,x='Installs',y='Rating')
y.set_title('Rating vs Installs [RegPlot]')
#Code ends here



# --------------
#Code starts here
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import seaborn as sns
#Code starts here
d=data['Price'].value_counts()
print(d)
data['Price']=data['Price'].apply(lambda x : x.replace('$',''))
d=data['Price'].value_counts()
print(d)
data['Price']=data['Price'].astype(float)
#le=LabelEncoder()
#data['Installs'] = le.fit_transform(data['Installs'])
y=sns.regplot(data=data,x='Price',y='Rating')
y.set_title('Rating vs Installs [RegPlot]')


#Code ends here


# --------------

#Code starts here

#print(data.head())
data['Genres']=data['Genres'].str.split(';').str[0]
#print(data['Genres'])
df=data[['Genres','Rating']]
gr_mean=df.groupby(['Genres'],as_index=False).mean()
#print(df['gr_mean'])
#print(gr_mean.describe())

gr_mean=gr_mean.sort_values(by=['Rating'])
#print(gr_mean[0,:])#,gr_mean[-1,:])
#Code ends heree


# --------------

#Code starts here
import seaborn as sns
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
print(data['Last Updated'].max())
max_date=data['Last Updated'].max()
data['Last Updated Days']=max_date-data['Last Updated']
data['Last Updated Days']=data['Last Updated Days'].dt.days

sns.regplot(data=data,x='Last Updated Days',y='Rating').set_title('Rating vs Last Updated [RegPlot]')


#Code ends here


