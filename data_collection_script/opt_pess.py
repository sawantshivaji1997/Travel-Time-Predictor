import time
import googlemaps
from datetime import datetime
import csv

gmaps=googlemaps.Client(key="AIzaSyD8j8hYdLvcXQVD6XjB95N7HD5BugOl7BE")
i=0
while(i<100):
    ################################################################Routes
    start1='114, Ganeshkhind Rd, ICS Colony, Ashok Nagar, Pune, Maharashtra 411007'
    end1='Pune Station Bus Stand, Agarkar Nagar, Pune, Maharashtra 411001'
    start2='Katraj PMPML Bus Depot, 29/44, Pune - Bengaluru Hwy, Kala Nagar, Dhankawadi, Pune, Maharashtra 411043'
    end2='Pune Station Bus Stand, Agarkar Nagar, Pune, Maharashtra 411001'
    start3='Borivali West, Mumbai, Maharashtra'
    end3='Andheri West, Mumbai, Maharashtra'
    
    start4='Hinjewadi Rajiv Gandhi Infotech Park, Hinjawadi, Pune, Maharashtra'
    end4='Rainbow Plaza, Dwarkadheesh Gardens, Pimple Saudagar, Pimpri-Chinchwad, Maharashtra 411027'
    
    start5='Rainbow Plaza, Dwarkadheesh Gardens, Pimple Saudagar, Pimpri-Chinchwad, Maharashtra 411027'
    end5='Hinjewadi Rajiv Gandhi Infotech Park, Hinjawadi, Pune, Maharashtra'
    
    start6='Ambience Mall, Gurgaon, Ambience Island, NH- 8,, DLF-3, Sector-24, Gurugram, Haryana 122002'
    end6='Delhi Cantonment, New Delhi, Delhi'
    
    start7='Howrah Railway Station, Howrah, West Bengal'
    end7='Dakshineswar Kali Temple, Dakshineswar, Kolkata, West Bengal 700076'
    
    start8='T. Anjaiah Lumbini Park, Opposite Secretariat New Gate, Khairatabad, Hyderabad, Telangana 500004'
    end8='Military Dairy Farm, Kistamma Enclave, Alwal, Hyderabad, Telangana 500011'
    #######################################get the joson file response from googlemaps####################################################
    ###########################################################################for route1
    car1=gmaps.distance_matrix(start1,end1, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car1["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist1 = temp["distance"]["value"]
    ctime1 = temp["duration_in_traffic"]["value"]  # duration
    ctime1=(int(ctime1))/60
   
    
    ###########################################################################for route2
    car2=gmaps.distance_matrix(start2,end2, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car2["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist2 = temp["distance"]["value"]
    ctime2 = temp["duration_in_traffic"]["value"]  # duration
    ctime2=(int(ctime2))/60
    
    
    ############################################################################for route3
    car3=gmaps.distance_matrix(start3,end3, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car3["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist3 = temp["distance"]["value"]
    ctime3 = temp["duration_in_traffic"]["value"]  # duration
    ctime3=(int(ctime3))/60
    
    
    ############################################################################for route4
    car4=gmaps.distance_matrix(start4,end4, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car4["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist4 = temp["distance"]["value"]
    ctime4 = temp["duration_in_traffic"]["value"]  # duration
    ctime4=(int(ctime4))/60
    
   
    ############################################################################for route5
    car5=gmaps.distance_matrix(start5,end5, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car5["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist5 = temp["distance"]["value"]
    ctime5 = temp["duration_in_traffic"]["value"]  # duration
    ctime5=(int(ctime5))/60
    
   
    ############################################################################for route6
    car6=gmaps.distance_matrix(start6,end6, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car6["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist6 = temp["distance"]["value"]
    ctime6 = temp["duration_in_traffic"]["value"]  # duration
    ctime6=(int(ctime6))/60
    
  
    ############################################################################for route7
    car7=gmaps.distance_matrix(start7,end7, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car7["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist7 = temp["distance"]["value"]
    ctime7 = temp["duration_in_traffic"]["value"]  # duration
    ctime7=(int(ctime7))/60
    
   
    ############################################################################for route8
    car8=gmaps.distance_matrix(start8,end8, mode="driving",departure_time=datetime.now(), traffic_model="pessimistic")
    temp= car8["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist8 = temp["distance"]["value"]
    ctime8 = temp["duration_in_traffic"]["value"]  # duration
    ctime8=(int(ctime8))/60
    
    ###################################################################
    print '#############################car8'
    print car8
    
    
    
    
    
    ############################################################get current time and date
    timee=datetime.now().time().strftime("%H:%M:%S")
    datee=datetime.now().strftime("%d/%m/%Y")
    currentDay1 = int(datetime.now().day)
    h,m,s=timee.split(':')
    timee1=float(float(h)*60+float(m)+float(float(s)/60))
    print datee
    
    print timee1
    
    if(currentDay1==1):
    	currentDay="Sunday"
    elif(currentDay1==2):
    	currentDay="Monday"
    elif(currentDay1==3):
    	currentDay="Tuesday"
    elif(currentDay1==4):
    	currentDay="Wednesday"
    elif(currentDay1==5):
    	currentDay="Thursday"
    elif(currentDay1==6):
    	currentDay="Friday"
    elif(currentDay1==7):
    	currentDay="Saturday"
    	
    print currentDay
    	
    
    
    #datte=datee.strftime("%d:%m:%Y")
    ###########################################################Writing to the file
    
    if(timee>=480 and timee<540):
        with open('pslot1.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'1',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=540 and timee<600):
        with open('pslot2.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'2',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=600 and timee<660):
        with open('pslot3.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'3',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=660 and timee<720):
        with open('pslot4.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'4',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
            
    elif(timee>=720 and timee<780):
        with open('pslot5.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'5',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=780 and timee<840):
        with open('pslot6.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'6',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=840 and timee<900):
        with open('pslot7.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'7',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=900 and timee<960):
        with open('pslot8.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'8',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=960 and timee<1020):
        with open('pslot9.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'9',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1020 and timee<1080):
        with open('pslot10.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'10',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1080 and timee<1140):
        with open('pslot11.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'11',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1140 and timee<1200):
        with open('pslot12.csv') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'12',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1200 and timee<1260):
        with open('pslot13.csv') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'13',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
    
    else:
    	with open('data123.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'1',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        	
    #######################################get the joson file response from googlemaps####################################################
    ###########################################################################for route1
    car1=gmaps.distance_matrix(start1,end1, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car1["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist1 = temp["distance"]["value"]
    ctime1 = temp["duration_in_traffic"]["value"]  # duration
    ctime1=(int(ctime1))/60
   
    
    ###########################################################################for route2
    car2=gmaps.distance_matrix(start2,end2, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car2["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist2 = temp["distance"]["value"]
    ctime2 = temp["duration_in_traffic"]["value"]  # duration
    ctime2=(int(ctime2))/60
    
    
    ############################################################################for route3
    car3=gmaps.distance_matrix(start3,end3, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car3["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist3 = temp["distance"]["value"]
    ctime3 = temp["duration_in_traffic"]["value"]  # duration
    ctime3=(int(ctime3))/60
    
    
    ############################################################################for route4
    car4=gmaps.distance_matrix(start4,end4, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car4["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist4 = temp["distance"]["value"]
    ctime4 = temp["duration_in_traffic"]["value"]  # duration
    ctime4=(int(ctime4))/60
    
   
    ############################################################################for route5
    car5=gmaps.distance_matrix(start5,end5, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car5["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist5 = temp["distance"]["value"]
    ctime5 = temp["duration_in_traffic"]["value"]  # duration
    ctime5=(int(ctime5))/60
    
   
    ############################################################################for route6
    car6=gmaps.distance_matrix(start6,end6, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car6["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist6 = temp["distance"]["value"]
    ctime6 = temp["duration_in_traffic"]["value"]  # duration
    ctime6=(int(ctime6))/60
    
  
    ############################################################################for route7
    car7=gmaps.distance_matrix(start7,end7, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car7["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist7 = temp["distance"]["value"]
    ctime7 = temp["duration_in_traffic"]["value"]  # duration
    ctime7=(int(ctime7))/60
    
   
    ############################################################################for route8
    car8=gmaps.distance_matrix(start8,end8, mode="driving",departure_time=datetime.now(), traffic_model="optimistic")
    temp= car8["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist8 = temp["distance"]["value"]
    ctime8 = temp["duration_in_traffic"]["value"]  # duration
    ctime8=(int(ctime8))/60
    
    ###################################################################
    print '#############################car8'
    print car8
    
    ############################################################get current time and date
    timee=datetime.now().time().strftime("%H:%M:%S")
    datee=datetime.now().strftime("%d/%m/%Y")
    currentDay1 = int(datetime.now().day)
    h,m,s=timee.split(':')
    timee1=float(float(h)*60+float(m)+float(float(s)/60))
    print datee
    
    print timee1
    
    if(currentDay1==1):
    	currentDay="Sunday"
    elif(currentDay1==2):
    	currentDay="Monday"
    elif(currentDay1==3):
    	currentDay="Tuesday"
    elif(currentDay1==4):
    	currentDay="Wednesday"
    elif(currentDay1==5):
    	currentDay="Thursday"
    elif(currentDay1==6):
    	currentDay="Friday"
    elif(currentDay1==7):
    	currentDay="Saturday"
    	
    print currentDay
    	
    
    
    #datte=datee.strftime("%d:%m:%Y")
    ###########################################################Writing to the file
    
    if(timee>=480 and timee<540):
        with open('oslot1.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'1',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=540 and timee<600):
        with open('oslot2.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'2',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=600 and timee<660):
        with open('oslot3.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'3',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=660 and timee<720):
        with open('oslot4.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'4',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
            
    elif(timee>=720 and timee<780):
        with open('oslot5.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'5',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=780 and timee<840):
        with open('oslot6.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'6',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=840 and timee<900):
        with open('oslot7.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'7',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=900 and timee<960):
        with open('oslot8.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'8',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=960 and timee<1020):
        with open('oslot9.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'9',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1020 and timee<1080):
        with open('oslot10.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'10',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1080 and timee<1140):
        with open('oslot11.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'11',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1140 and timee<1200):
        with open('oslot12.csv') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'12',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
        
        
    elif(timee>=1200 and timee<1260):
        with open('oslot13.csv') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'13',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
    
    else:
    	with open('data123.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'1',ctime1,ctime2,ctime3,ctime4,ctime5,ctime6,ctime7,ctime8,'N'])
    ##########################################################Waiting
    i=i+1
    time.sleep(450)
