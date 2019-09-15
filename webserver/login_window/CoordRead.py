import random
import time
import math

def CoordRead():
    ## Read file and give coordinates as list of tuples.
    filename = input("Give filename: ")
    
    coordinates = open(filename)
    content = coordinates.read()
    cords = content.splitlines()
    n_cords = [eval(elt) for elt in cords]
    
    ## Use current time to determine threshold value for avaliable parking.
    locTime = time.localtime()
    time_current = time.strftime("%H:%M:%S", locTime)
    Hr = int(locTime[3])
    Min = int(locTime[4])
    Sec = int(locTime[5])

    AvaCordList = []

    ## Percentage Time Model with static values
    ##NonHours = {0:0.95 ,  1:0.90 , 2:0.85 ,
    #             3:0.76 ,  4:0.65 , 5:0.60 ,
    #             6:0.56 ,  7:0.50 , 8:0.40 ,
    #             9:0.35 ,  10:0.36, 11:0.33,  
    #             12:0.21, 13:0.25, 14:0.34,
    #             15:0.40, 16:0.46, 17:0.50,
    #             18:0.56, 19:0.62, 20:0.70,
    #             21:0.75, 22:0.83, 23:0.90}

    ## Percentage Time Model using functions
    NonHours2 = []
    x = list(range(1440))
    for num in x :
        y = math.sin(12 * math.pi * (num/60)) * .5 + .5 ## Test function
        NonHours2 = NonHours2 + [y]
    
    FullMin = Hr*60 + Min;
    Nonavailability = NonHours2[FullMin]
    for i in n_cords:
        rng = random.random()
        if rng > Nonavailability:
            AvaCordList = AvaCordList + [i]

    coordinates.close()
    return AvaCordList


            
            
            

    


 
