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

print("Enter Hours:")
hours=int(input())
print("Enter Minutes:")
minutes=int(input())
print("Enter Seconds:")
seconds=int(input())
c='Car'
b='Bus'
#print("Enter Mode of Transport:")
#mode=raw_input()
print("Enter route:")
route=int(input())
reg=LinearRegression()
to_mins=minutes+hours*60+seconds/60

#traffic=pd.read_csv('slot1.csv')
#X=traffic['to_minutes'].values
#X=X.reshape(-1,1)

#'''
def qwe(to_mins,route):
    if(to_mins>=480 and to_mins<540):
        traffic=pd.read_csv('slot1.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=540 and to_mins<600):
        traffic=pd.read_csv('slot2.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=600 and to_mins<660):
        traffic=pd.read_csv('slot3.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=660 and to_mins<720):
        traffic=pd.read_csv('slot4.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)    
    elif(to_mins>=720 and to_mins<780):
        traffic=pd.read_csv('slot5.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=780 and to_mins<840):
        traffic=pd.read_csv('slot6.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=840 and to_mins<900):
        traffic=pd.read_csv('slot7.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=900 and to_mins<960):
        traffic=pd.read_csv('slot8.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=960 and to_mins<1020):
        traffic=pd.read_csv('slot9.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1020 and to_mins<1080):
        traffic=pd.read_csv('slot10.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1080 and to_mins<1140):
        traffic=pd.read_csv('slot11.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1140 and to_mins<1200):
        traffic=pd.read_csv('slot12.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1200 and to_mins<1260):
        traffic=pd.read_csv('slot13.csv')
        X=traffic['to_minutes'].values
        X=X.reshape(-1,1)
 # '''  
    ans 
    if(route==1):
        Y=traffic['car1'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus1'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
    
    elif(route==2):
        Y=traffic['car2'].values
            
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus2'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==3):
        Y=traffic['car3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==4):
        Y=traffic['car4'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus4'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
    elif(route==5):
        Y=traffic['car5'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus5'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
    elif(route==6):
        Y=traffic['car6'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus6'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
    elif(route==7):
        Y=traffic['car7'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus7'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
    elif(route==8):
        Y=traffic['car8'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        Y=traffic['bus8'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
    return ans