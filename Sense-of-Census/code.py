# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=',',skip_header=1)
#New record

new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record=np.array(new_record)
census=np.concatenate((data,new_record),axis=0)
print(census)
#Code starts here



# --------------
#Code starts here
age=census[:,0]

print(age)
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_mean=np.around(age_mean,decimals=2)
age_std=np.std(age)
print(max_age,min_age,age_mean,age_std)


# --------------
#Code starts here
#race=census[:,2]
#r#ace=np.array(race)
race_0=census[np.where(census[:,2]==0)]
print(race_0)
race_1=census[np.where(census[:,2]==1)]
print(race_1)
race_2=census[np.where(census[:,2]==2)]
print(race_2)
race_3=census[np.where(census[:,2]==3)]
print(race_3)
race_4=census[np.where(census[:,2]==4)]
print(race_4)
race_5=census[np.where(census[:,2]==5)]
print(race_5)

'''
race_1=np.array([i for i in race if i==1])
#print(race_1)
race_2=np.array([i for i in race if i==2])
#print(race_2)
race_3=np.array([i for i in race if i==3])
#print(race_3)
race_4=np.array([i for i in race if i==4])
#print(race_4)'''
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)

len_4=len(race_4)
minority_race=0
if len_0<len_1 and len_1<len_2 and len_2<len_3 and len_3<len_4:
    minority_race=0
elif len_1<len_0 and len_1<len_2 and len_1<len_3 and len_1<len_4:
    minority_race=1
elif len_2<len_0 and len_2<len_1 and len_2<len_3 and len_2<len_4:
    minority_race=2
elif len_3<len_0 and len_3<len_2 and len_3<len_1 and len_3<len_4:
    minority_race=3
elif len_4<len_0 and len_4<len_2 and len_4<len_3 and len_4<len_1:
    minority_race=4


print(minority_race)



# --------------
#Code starts here
#age = census[:,0]
senior_citizens=census[np.where(census[:,0]>60)]
#print(senior_citizens)
'''zip_1=zip(age,workinghours)
working_hour=[]
for x,y in zip_1:
    if x>60:
        working_hour.append(y)
'''
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len=len(senior_citizens)
#print(working_hour)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[np.where(census[:,1]>10)]
low=census[np.where(census[:,1]<=10)]
avg_pay_high=high.sum(axis=0)[7]/len(high)

avg_pay_low=np.around((low.sum(axis=0)[7]/len(low)),decimals=2)
print(avg_pay_low)

if avg_pay_high>avg_pay_low:
    print(True)




