import time
import googlemaps
from datetime import datetime
import csv

gmaps=googlemaps.Client(key="AIzaSyAbWeBHKYbaQniv--vMtDtY20qrFJqwBCw")
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
    car1=gmaps.distance_matrix(start1,end1, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car1["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist1 = temp["distance"]["value"]
    ctime1 = temp["duration_in_traffic"]["value"]  # duration
    ctime1=(int(ctime1))/60
    
    bus1=gmaps.distance_matrix(start1,end1, mode="transit",traffic_model="best_guess")
    temp= bus1["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist1 = temp["distance"]["value"]
    btime1 = temp["duration"]["value"]  # duration
    btime1=(int(btime1))/60
    
    ###########################################################################for route2
    car2=gmaps.distance_matrix(start2,end2, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car2["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist2 = temp["distance"]["value"]
    ctime2 = temp["duration_in_traffic"]["value"]  # duration
    ctime2=(int(ctime2))/60
    
    bus2=gmaps.distance_matrix(start2,end2, mode="transit",traffic_model="best_guess")
    temp= bus2["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist2 = temp["distance"]["value"]
    btime2 = temp["duration"]["value"]  # duration
    btime2=(int(btime2))/60
    ############################################################################for route3
    car3=gmaps.distance_matrix(start3,end3, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car3["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist3 = temp["distance"]["value"]
    ctime3 = temp["duration_in_traffic"]["value"]  # duration
    ctime3=(int(ctime3))/60
    
    bus3=gmaps.distance_matrix(start3,end3, mode="transit",traffic_model="best_guess")
    temp= bus3["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist3 = temp["distance"]["value"]
    btime3 = temp["duration"]["value"]  # duration
    btime3=(int(btime3))/60
    ############################################################################for route4
    car4=gmaps.distance_matrix(start4,end4, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car4["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist4 = temp["distance"]["value"]
    ctime4 = temp["duration_in_traffic"]["value"]  # duration
    ctime4=(int(ctime4))/60
    
    bus4=gmaps.distance_matrix(start4,end4, mode="transit",traffic_model="best_guess")
    temp= bus4["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist4 = temp["distance"]["value"]
    btime4 = temp["duration"]["value"]  # duration
    btime4=(int(btime4))/60
    ############################################################################for route5
    car5=gmaps.distance_matrix(start5,end5, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car5["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist5 = temp["distance"]["value"]
    ctime5 = temp["duration_in_traffic"]["value"]  # duration
    ctime5=(int(ctime5))/60
    
    bus5=gmaps.distance_matrix(start5,end5, mode="transit",traffic_model="best_guess")
    temp= bus5["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist5 = temp["distance"]["value"]
    btime5 = temp["duration"]["value"]  # duration
    btime5=(int(btime5))/60
    ############################################################################for route6
    car6=gmaps.distance_matrix(start6,end6, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car6["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist6 = temp["distance"]["value"]
    ctime6 = temp["duration_in_traffic"]["value"]  # duration
    ctime6=(int(ctime6))/60
    
    bus6=gmaps.distance_matrix(start6,end6, mode="transit",traffic_model="best_guess")
    temp= bus6["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist6 = temp["distance"]["value"]
    btime6 = temp["duration"]["value"]  # duration
    btime6=(int(btime6))/60
    ############################################################################for route7
    car7=gmaps.distance_matrix(start7,end7, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car7["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist7 = temp["distance"]["value"]
    ctime7 = temp["duration_in_traffic"]["value"]  # duration
    ctime7=(int(ctime7))/60
    
    bus7=gmaps.distance_matrix(start7,end7, mode="transit",traffic_model="best_guess")
    temp= bus7["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist7 = temp["distance"]["value"]
    btime7 = temp["duration"]["value"]  # duration
    btime7=(int(btime7))/60
    ############################################################################for route8
    car8=gmaps.distance_matrix(start8,end8, mode="driving",departure_time=datetime.now(), traffic_model="best_guess")
    temp= car8["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    cdist8 = temp["distance"]["value"]
    ctime8 = temp["duration_in_traffic"]["value"]  # duration
    ctime8=(int(ctime8))/60
    
    bus8=gmaps.distance_matrix(start8,end8, mode="transit",traffic_model="best_guess")
    temp= bus8["rows"][0]["elements"][0]
    assert temp["status"]=="OK"
    bdist8 = temp["distance"]["value"]
    btime8 = temp["duration"]["value"]  # duration
    btime8=(int(btime8))/60
    ###################################################################
    print '#############################car8'
    print car8
    print '#############################bus8'
    print bus8
    
    
    
    i=i+1
    
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
        with open('slot1.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'1',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=540 and timee<600):
        with open('slot2.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'2',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=600 and timee<660):
        with open('slot3.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'3',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=660 and timee<720):
        with open('slot4.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'4',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
            
    elif(timee>=720 and timee<780):
        with open('slot5.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'5',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=780 and timee<840):
        with open('slot6.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'6',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=840 and timee<900):
        with open('slot7.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'7',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=900 and timee<960):
        with open('slot8.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'8',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=960 and timee<1020):
        with open('slot9.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'9',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=1020 and timee<1080):
        with open('slot10.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'10',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=1080 and timee<1140):
        with open('slot11.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'11',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=1140 and timee<1200):
        with open('slot12.csv') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'12',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
        
        
    elif(timee>=1200 and timee<1260):
        with open('slot13.csv') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'13',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
    
    else:
    	with open('data123.csv','a') as newFile:
        	newFileWriter = csv.writer(newFile)
        	#newFileWriter.writerow(['date','actual time','car1','bus1','cab1','car2','bus2','cab2','car3','bus3','cab3','Holiday'])
        	newFileWriter.writerow([datee,currentDay,timee,timee1,'1',ctime1,btime1,ctime2,btime2,ctime3,btime3,ctime4,btime4,ctime5,btime5,ctime6,btime6,ctime7,btime7,ctime8,btime8,'N'])
    ##########################################################Waiting
   
    time.sleep(450)
