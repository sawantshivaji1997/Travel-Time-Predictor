import socket
import threading
import json
import ast
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
import os
import inspect
reg=LinearRegression()

def optimistic(to_mins,route):
    print inspect.getfile(inspect.currentframe())
    print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    if(to_mins>=480 and to_mins<540):
        trafficb=pd.read_csv('oslot1.csv')
        X=trafficb['to_minutes'].values

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
        Y=trafficb['bus3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
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
    return ans

def pessimistic(to_mins,route):
    print inspect.getfile(inspect.currentframe())
    print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    if(to_mins>=480 and to_mins<540):
        trafficb=pd.read_csv('pslot1.csv')
        X=trafficb['to_minutes'].values

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
        Y=trafficb['bus3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        print("Predicted Time by bus")
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
    return ans
    


def qwe(to_mins,route):
    print inspect.getfile(inspect.currentframe())
    print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
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
        traffic=pd.read_csv('slot7.csv')
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
        
     
    if(route==1):
        Y=traffic['car1'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus1'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans2=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
    
    elif(route==2):
        Y=traffic['car2'].values
            
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus2'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans2=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        
    elif(route==3):
        Y=traffic['car3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus3'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans2=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        
    elif(route==4):
        Y=traffic['car4'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus4'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans2=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
    elif(route==5):
        Y=traffic['car5'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus5'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
    elif(route==6):
        Y=traffic['car6'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus6'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans2=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
    elif(route==7):
        Y=traffic['car7'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus7'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans2=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
    elif(route==8):
        Y=traffic['car8'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by car")
    	ans1=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
        Y=traffic['bus8'].values
        
        Y=Y.reshape(-1,1)
        X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)
        reg.fit(X_train,y_train)
        y_pred=reg.predict(X_test)
        #print("Predicted Time by bus")
    	ans2=reg.predict(to_mins)
    	
    	#print (str(int(ans))+" minutes")
    return ans1,ans2
    
class test(object):
	def __init__(self, t, route):
	        self.t = t
	        self.route = route
	        
	def graph():
    		val=492%30
    		route=3
    		i=480+val
    		listx=[]
   
   	 	listycb=[]   # best guess for car   
    		listyco=[]    #optimistic for car
    		listycp=[]  #pessimistic for car
    		listybus=[] # best guess bus
    		print('outside while')
    		while(i<1260):
       		 	listx.append(i)
       		 	a,b=qwe(t,route)
       		 	listycb.append(a)
        		listybus.append(b)
        		print('inside while')
        		o=opt(t,route)  #optimistic function call
        		p=pess(t,route) #pessimistic function call
        		listyco.append(o)
        		listycp.append(p)
        		i=i+30
   	 	print(listx)
   	 	print(listycb)
   	 	print(listyco)
   	 	print(listycp)
   	 	print(listbus)    
    
'''
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 4096
        while True:
            #try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    print response
                    #response=str(response)
                    o=json.dumps(response)
                    n=json.loads(o)
                    with open('data.txt','w') as g:
                        json.dump(o,g)
                        
                    ad = ast.literal_eval(n)
                    print(type(ad))   
                    y=ad['Time']
                    print(y)    
                    t=ad['Time']
                    r=ad['Route']
                    print ("qwert")
                    
     
                        
                    print("fghj")
                    a,b=qwe(t,r) 
                    data_to_send={"Car_best_guess":a,"Car_opt":"20","Car_pess":"20","Bus":b,
                    "X_axis":[],
                    "best_guess":[]}
                    print ("asxasc"+str(a))
                    data_to_send=str(data_to_send)
                    client.send(data_to_send)
                    client.close()
                else:
                    raise ValueError('Client disconnected')
            #except:
            #	print("asd")
             #   client.close()
              #  return False
              '''

if __name__ == "__main__":
    while True:
        #port_num = input("Port? ")
        try:
            #port_num = int(port_num)
            break
        except ValueError:
            pass

    test(492,3)
