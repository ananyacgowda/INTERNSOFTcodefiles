
"""
Created on Wed Sep  6 21:05:56 2023

@author: anany
"""


#IMPORTING THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt



# READING THE DATA FROM YOUR FILES
data = pd.read_csv("advertising.csv")
data.head()




#TO VISUALISE DATA
fig , axs = plt.subplots(1,3,sharey = True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])


#CREATING X&Y FOR LINEAR REGRESSION
feature_cols = ['TV']
x = data[feature_cols]
y = data.Sales



#IMPORTING LINEAR REGRESSION ALGO FOR SIMPLE LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
lr =  LinearRegression()
lr.fit(x,y)



print(lr.intercept_)
print(lr.coef_)







result = 6.97+0.0554*50
print(result)


#CREATING A DATAFRAME WITH MIN AND MAX VALUE OF THE TABLE
X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
X_new.head()



preds = lr.predict(X_new)
preds


data.plot(kind = 'scatter',x='TV',y='Sales')


plt.plot(X_new,preds,c='red',linewidth = 3)


import statsmodels.formula.api as smf
lm = smf.ols(formula = 'Sales ~ TV',data = data).fit()
lm.conf_int()



#FINDING THE PROBABILITY VALUES
lm.pvalues



#FINDING THE R-SQUARED VALUES
lm.rsquared



#MULTI LINEAR REGRESSION
feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales


lr = LinearRegression()
lr.fit(X,y)


print(lr.intercept_)
print(lr.coef_)



lm = smf.ols(formula='Sales ~ TV+Radio+Newspaper',data=data).fit()
lm.conf_int()
lm.summary()
























































