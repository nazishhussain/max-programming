import RPi.GPIO as GPIO  
import time  
 # Trigger Pin  
Trigger = 18  
Echo = 24 
GPIO.setmode( GPIO.BOARD)  
GPIO.setup( Trigger, GPIO.OUT) 
GPIO.setup( Echo, GPIO.IN)  
print("Starting program" ) 
try:
    while True:
        GPIO.output( Trigger, True)
        time.sleep(2)
        GPIO.output(Trigger, False)
        time.sleep(0.00001)
        GPIO.output(Trigger, False)
    while GPIO.input(Echo)==0:
            start_time = time.time()
    while GPIO.input(Echo)==1:
            end_time = time.time()
            tof = end_time - start_time  
            print("Time of Flight = ", tof, " sec")
    distance = (tof * 34300.0) / 2.0
    distance = round(distance, 2)
    print (" Object Distance = ", distance, " cm")
except KeyboardInterrupt:  
    print ("Exiting Program" )
except:  
    print ("Error Occurs, Exiting Program")
finally:  
    GPIO.cleanup()  
