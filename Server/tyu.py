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




if True:
    if(to_mins>=480 and to_mins<540):
        trafficb=pd.read_csv('oslot1.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
	print("asdasd")

    elif(to_mins>=540 and to_mins<600):
        trafficb=pd.read_csv('oslot2.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
        
        
    elif(to_mins>=600 and to_mins<660):
        trafficb=pd.read_csv('oslot3.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
        
        
    elif(to_mins>=660 and to_mins<720):
        trafficb=pd.read_csv('oslot4.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)    
       
    elif(to_mins>=720 and to_mins<780):
        trafficb=pd.read_csv('oslot5.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=780 and to_mins<840):
        trafficb=pd.read_csv('oslot6.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=840 and to_mins<900):
        trafficb=pd.read_csv('oslot7.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=900 and to_mins<960):
        trafficb=pd.read_csv('oslot8.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=960 and to_mins<1020):
        trafficb=pd.read_csv('oslot9.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1020 and to_mins<1080):
        trafficb=pd.read_csv('oslot10.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1080 and to_mins<1140):
        trafficb=pd.read_csv('oslot11.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1140 and to_mins<1200):
        trafficb=pd.read_csv('oslot12.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1200 and to_mins<1260):
        trafficb=pd.read_csv('oslot13.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
        
     
    if(route==1):
        Y=trafficb['car1'].values
        print("qwe")
        
        Y=Y.reshape(-1,1)
        print(X)
        print(Y)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        print("rty")
        reg.fit(X_train,y_train)
        print("uio")
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    
    elif(route==2):
        Y=trafficb['car2'].values
            
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
        
    elif(route==3):
        Y=trafficb['car3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
        
    elif(route==4):
        Y=trafficb['car4'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==5):
        Y=trafficb['car5'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==6):
        Y=trafficb['car6'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==7):
        Y=trafficb['car7'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==8):
        Y=trafficb['car8'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
  
if True:
    if(to_mins>=480 and to_mins<540):
        trafficb=pd.read_csv('pslot1.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
        print("Hello")
        
    elif(to_mins>=540 and to_mins<600):
        trafficb=pd.read_csv('pslot2.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
        
        
    elif(to_mins>=600 and to_mins<660):
        trafficb=pd.read_csv('pslot3.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
        
        
    elif(to_mins>=660 and to_mins<720):
        trafficb=pd.read_csv('pslot4.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)    
       
    elif(to_mins>=720 and to_mins<780):
        trafficb=pd.read_csv('pslot5.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=780 and to_mins<840):
        trafficb=pd.read_csv('pslot6.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=840 and to_mins<900):
        trafficb=pd.read_csv('pslot7.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=900 and to_mins<960):
        trafficb=pd.read_csv('pslot8.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=960 and to_mins<1020):
        trafficb=pd.read_csv('pslot9.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1020 and to_mins<1080):
        trafficb=pd.read_csv('pslot10.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1080 and to_mins<1140):
        trafficb=pd.read_csv('pslot11.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1140 and to_mins<1200):
        trafficb=pd.read_csv('pslot12.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
    elif(to_mins>=1200 and to_mins<1260):
        trafficb=pd.read_csv('pslot13.csv')
        X=trafficb['to_minutes'].values
        X=X.reshape(-1,1)
        
     
    if(route==1):
        Y=trafficb['car1'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    
    elif(route==2):
        Y=trafficb['car2'].values
            
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
        
    elif(route==3):
        Y=trafficb['car3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
        
    elif(route==4):
        Y=trafficb['car4'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==5):
        Y=trafficb['car5'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==6):
        Y=trafficb['car6'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==7):
        Y=trafficb['car7'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
        
    elif(route==8):
        Y=trafficb['car8'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by car")
    	ans=reg.predict(to_mins)
    	
    	print (str(int(ans))+" minutes")
   # return ans[0][0]

