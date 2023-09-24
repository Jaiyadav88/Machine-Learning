import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
df=pd.read_csv('homeprices_2.csv')
df.head()
df.isnull().sum()
plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['area'],df['price'],marker='o',color='red')
plt.title('Area VS Price')
plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['age'],df['price'],marker='o',color='red')
plt.title('Age VS Price')
plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['bedrooms'],df['price'],marker='o',color='red')
plt.title(' Bedrooms VS Price')


#independent variables
x=df[['area','age','bedrooms']]
#dependent variable
y=df.price
model=linear_model.LinearRegression()
model.fit(x,y) # it will fit the data and find intercept and coefficient
model.coef_
model.intercept_
area=int(input("Enter the area"))
bedroom=int(input("Enter the bedrooms:"))
age=int(input("Enter the age:"))
result=model.predict([[area,bedroom,age]])
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
df=pd.read_csv('homeprices_2.csv')
df.head()
df.isnull().sum()
plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['area'],df['price'],marker='o',color='red')
plt.title('Area VS Price')
plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['age'],df['price'],marker='o',color='red')
plt.title('Age VS Price')
plt.figure()
plt.title('Area Vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df['bedrooms'],df['price'],marker='o',color='red')
plt.title(' Bedrooms VS Price')


#independent variables
x=df[['area','age','bedrooms']]
#dependent variable
y=df.price
model=linear_model.LinearRegression()
model.fit(x,y) # it will fit the data and find intercept and coefficient
model.coef_
model.intercept_
area=int(input("Enter the area"))
bedroom=int(input("Enter the bedrooms:"))
age=int(input("Enter the age:"))
result=model.predict([[area,bedroom,age]])
print(f'The prediction is:${result}')