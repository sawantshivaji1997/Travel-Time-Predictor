from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


traffic=pd.read_csv('slot10.csv')

X=traffic['to_minutes'].values
X = X[np.logical_not(np.isnan(X))]
Y=traffic['car3'].values
Y = Y[np.logical_not(np.isnan(Y))]

X=X.reshape(-1,1)
Y=Y.reshape(-1,1)
X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)

reg=LinearRegression()

reg.fit(X_train,y_train)

y_pred=reg.predict(X_test)

#plt.scatter(X_test,y_pred,color='blue',linewidth=3)
#plt.show()

to_minx=[1020,1030,1040,1050,1060,1070,1080]
to_min_labelx=['17:00','17:10','17:20','17:30','17:40','17:50','18:00']

to_miny=[50,55,60,65,70,75,80,85]
#to_min_labely=['1','17:10','17:20','17:30','17:40','17:50','18:00']

#plt.scatter(X_train,y_train,color='black',marker="o",s=30)
#plt.plot(X_test,y_pred,color='red',linewidth=3)
plt.title("Sample Graph to analyze variation in traffic")
#plt.hist(Y)
#plt.xticks(to_minx,to_min_labelx)
#plt.yticks((to_miny))
x_1=[1020,1030,1040,1050,1060,1070,1080]
y_1=[10,50,55,70,43,67,87]

plt.plot(x_1,y_1)
#plt.xlabel('Duration',color='Blue',size=15)
#plt.ylabel('Frequency',color='blue',size=15)
#cv_scores = cross_val_score(reg,X,Y,cv=5)
#print(cv_scores)
#print(confusion_matrix(y_test, y_pred))
#print(classification_report(y_test, y_pred))
plt.show()
    	
  
   
    	
    	
    	
    	
             	
    	
    

	
	








