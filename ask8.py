print("Exersice 8\n")
import random #import the function random in order to give us the random numbers of the cars each traffic light has
#the radint() method returns an integer number selected element from the specified range
trl1 = random.randint(1,50) #guessing that the max number of cars each traffic light can have at the starting point is 50
trl2 = random.randint(1,50)
trl3 = random.randint(1,50)
print("Traffic light 1:",trl1,"\nTraffic light 2:",trl2,"\nTraffic light 3:",trl3,"\n")

def finding_max(trl1,trl2,trl3): #a function in order to find max
    max = trl1
    if trl2 > max:
        max = trl2
    elif trl2 == max:
        r = random.randint(1,2) #if the traffic lights have the same amount of cars then the max is selected randomly 
        if r == 1:
            max = trl1
        else:
            max = trl2
    if trl3 > max :
         max = trl3
    elif trl3 == max:
        r = random.randint(2,3) #if the traffic lights have the same amount of cars then the max is selected randomly
        if r == 2:
            max = trl2
        else:
            max = trl3

while trl1 > 0 and trl2 > 0 and trl3 > 0: #the loop stops when 1 or more traffic lights have 0 cars
    
    max = finding_max(trl1,trl2,trl3)

    if max == trl1:
        print ("Traffic Light 1 is green\n")
        l = random.randint(5,10) #the cars that leave while the light is green
        print ("While the traffic light is green, ",l,"cars leave\n")
        trl1 -= l  
        print ("Traffic Light 1 has ",trl1,"cars\n")
        m2 = random.randint(0,5) #the cars that are waiting to the traffic light 2
        print (m2," cars are added to the traffic light 2\n")
        trl2 += m2
        print ("Traffic Light 2 is red and has ",trl2,"cars\n")
        m3 = random.randint(0,5) #the cars that are waiting to the traffic light 3
        print (m3," cars are added to the traffic light 3\n")
        trl3 += m3
        print ("Traffic Light 3 is red and has ",trl3,"cars\n")
    elif max == trl2:
        print ("Traffic Light 2 is green\n")
        l = random.randint(5,10) #the cars that leave while the light is green
        print ("While the traffic light is green, ",l,"cars leave\n")
        trl1 -= l  
        print ("Traffic Light 2 has ",trl2,"cars\n")
        m1 = random.randint(0,5) #the cars that are waiting to the traffic light 1
        print (m1," cars are added to the traffic light 1\n")
        trl1 += m1
        print ("Traffic Light 1 is red and has ",trl1,"cars\n")
        m3 = random.randint(0,5) #the cars that are waiting to the traffic light 3
        print (m3," cars are added to the traffic light 3\n")
        trl3 += m3
        print ("Traffic Light 3 is red and has ",trl3,"cars\n")
    else:
        print ("Traffic Light 3 is green\n")
        l = random.randint(5,10) #the cars that leave while the light is green
        print ("While the traffic light is green, ",l,"cars leave\n")
        trl1 -= l  
        print ("Traffic Light 3 has ",trl1,"cars\n")
        m1 = random.randint(0,5) #the cars that are waiting to the traffic light 1
        print (m1," cars are added to the traffic light 1\n")
        trl1 += m1
        print ("Traffic Light 1 is red and has ",trl1,"cars\n")
        m2 = random.randint(0,5) #the cars that are waiting to the traffic light 2
        print (m2," cars are added to the traffic light 2\n")
        trl2 += m2
        print ("Traffic Light 2 is red and has ",trl2,"cars\n")
       
