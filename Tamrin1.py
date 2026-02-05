import pandas as pd
import numpy as np
from scipy import stats as st
print('-'*100)
print('-'*100)

#Creating a csv file
peopleDF=pd.DataFrame([
    {'Name':'Ali','Age':25,'Height':174,'Weight':69,'Gender':'Male',
        'Hobby':'Music','City':'Tehran','Education':'Bachelor','MaritalStatus':'Single'},
    {'Name':'Ahmad','Age':30,'Height':191,'Weight':88,'Gender':'Male',
        'Hobby':'Sports','City':'Shiraz','Education':'Master','MaritalStatus':'Married'},
    {'Name':'Sara','Age':22,'Height':168,'Weight':65,'Gender':'Female',
        'Hobby':'Movies','City':'Esfahan','Education':'PhD','MaritalStatus':'Single'},
    {'Name':'Reza','Age':35,'Height':178,'Weight':94,'Gender':'Male',
        'Hobby':'History','City':'Tabriz','Education':'Bachelor','MaritalStatus':'Married'},
    {'Name':'Narges','Age':28,'Height':159,'Weight':57,'Gender':'Female',
        'Hobby':'Travel','City':'Mashhad','Education':'Master','MaritalStatus':'Single'}
                    ])
print('peopleDF:\n',peopleDF)
print('-'*100)

#Saving the dataframe as csv
peopleDF.to_csv('people.csv', index=False)

#Mean and median of age and weight
meanAge=np.mean(peopleDF.Age)
medianAge=np.median(peopleDF.Age)
print('mean age=',meanAge)
print('median age=',medianAge)
meanWeight=np.mean(peopleDF.Weight)
medianWeight=np.median(peopleDF.Weight)
print('mean weighte=',meanWeight )
print('median weight=',medianWeight)
print('-'*100)

#Mode for height, gender,education
modeHeight = peopleDF['Height'].mode()
print('mode of height=',modeHeight)
print('ATTENTION! Height has no mode as all values are unique')
modeGender = peopleDF['Gender'].mode()
print('mode of gender=',modeGender)
modeEducation = peopleDF['Education'].mode()
print('mode of education=',modeEducation)
print('-'*100)

#Range of age, height and weight
rangeAge= np.max(peopleDF.Age)-np.min(peopleDF.Age)
print('age range=',rangeAge)
rangeHeight= np.max(peopleDF.Height)-np.min(peopleDF.Height)
print('height range=',rangeHeight)
rangeWeight= np.max(peopleDF.Weight)-np.min(peopleDF.Weight)
print('weight range=',rangeWeight)
print('-'*100)

#Variance and SD of age, height and weight
varAge= np.var(peopleDF.Age)
print('age variance=',varAge)
varHeight= np.var(peopleDF.Height)
print('height variance=',varHeight)
varWeight= np.var(peopleDF.Weight)
print('weight variance=',varWeight)

stdAge= np.std(peopleDF.Age).round(2)
print('age std=',stdAge)
stdHeight= np.std(peopleDF.Height).round(2)
print('height std=',stdHeight)
stdWeight= np.std(peopleDF.Weight).round(2)
print('weight std=',stdWeight)
print('-'*100)

#1st, 2nd and 3rd quartiles of age, height and weight
q1Age= np.percentile(peopleDF.Age,25).astype(int)
print('Q1 of age=',q1Age)
q2Age= np.percentile(peopleDF.Age,50).astype(int)
print('Q2 of age=',q2Age)
q3Age= np.percentile(peopleDF.Age,75).astype(int)
print('Q3 of age=',q3Age)

q1Height= np.percentile(peopleDF.Height,25).astype(int)
print('Q1 of height=',q1Height)
q2Height= np.percentile(peopleDF.Height,50).astype(int)
print('Q2 of height=',q2Height)
q3Height= np.percentile(peopleDF.Height,75).astype(int)
print('Q3 of height=',q3Height)

q1Weight= np.percentile(peopleDF.Weight,25).astype(int)
print('Q1 of weight=',q1Weight)
q2Weight= np.percentile(peopleDF.Weight,50).astype(int)
print('Q2 of weight=',q2Weight)
q3Weight= np.percentile(peopleDF.Weight,75).astype(int)
print('Q3 of weight=',q3Weight)
print('-'*100)

#IQR of age, height and weight
iqrAge= q3Age-q1Age
print('IQR of age=',iqrAge)
iqrHeight= q3Height-q1Height
print('IQR of Height=',iqrHeight)
iqrWeight= q3Weight-q1Weight
print('IQR of Weight=',iqrWeight)
print('-'*100)
print('-'*100)

