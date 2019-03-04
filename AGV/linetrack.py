# -*- coding: UTF-8 -*- 
#!/usr/bin/env python 
import cv2
#import pwm_motor as motor
#import dc_motor as motor
import RPi.GPIO as GPIO
import time
TRIG=16
Echo=18
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)  #forward
GPIO.setup(11,GPIO.OUT) #right
GPIO.setup(13,GPIO.OUT)#left
GPIO.setup(19,GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)#echo
GPIO.setup(Echo, GPIO.IN)#trig, initial=GPIO.LOW
#GPIO.setup(15,GPIO.OUT) #accelation
Color_Lower = (0, 123,100)
Color_Upper = (5, 255, 255)
Color_Lower1 = (78, 43,46)
Color_Upper1 = (110, 255, 255)
Frame_Width  = 320
Frame_Height = 240
flag1=0
flag2=0
flag3=0
flagb=0
camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH,  Frame_Width)

camera.set(cv2.CAP_PROP_FRAME_HEIGHT, Frame_Height)



try:
    GPIO.output(13,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)   
    GPIO.output(19,GPIO.LOW)
    
    def get_distance():

        GPIO.output(16, False)
        time.sleep(2)
        GPIO.output(16, True)
        time.sleep(0.00001)
        GPIO.output(16, False)

        while GPIO.input(18)==0:
            start = time.time()

        while GPIO.input(18)==1:
            end = time.time()

        return (end - start) * 17150
    while True:

        
        (_, frame) = camera.read()
        
        # Do gaussian blur if needed

        frame = cv2.GaussianBlur(frame, (11, 11), 0)  

        # Convert to HSV color space

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Convert to binary with given color

        mask = cv2.inRange(hsv, Color_Lower, Color_Upper)
        mask1 = cv2.inRange(hsv, Color_Lower1, Color_Upper1)
        
        # Do erode if needed

        #mask = cv2.erode(mask, None, iterations=2)



        # Do dilate if needed

        #mask = cv2.dilate(mask, None, iterations=2)



        # Find the contours

        (_, contours, hier) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        (_, contours1, hier) = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #(contours, _) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Define mass center

        center = None    
        center1 = None 

        if len(contours) > 0:

            # Find the max length of contours

            c = max(contours, key=cv2.contourArea)


            # Find the x, y, radius of given contours        

            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # Find the moments

            M = cv2.moments(c)
            
        if len(contours1) > 0:

            # Find the max length of contours

            c1 = max(contours1, key=cv2.contourArea)


            # Find the x, y, radius of given contours        

            ((x1, y1), radius1) = cv2.minEnclosingCircle(c1)

            # Find the moments

            M1 = cv2.moments(c1)

            if flagb==0:
                try:    #detect color blue then turn right

                    # mass center

                    center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))


                    # process every frame

                    cv2.circle(frame, (int(x1), int(y1)), int(radius1),(255, 255, 0), 2)

                    cv2.circle(frame, center1, 5, (0, 0, 255), -1)

                    if center1[1] > Frame_Height/2-43:#turnRight
                        flag3=flag3+1
                        if(flag3>=10):
                            print("blue turnright")
                            GPIO.output(13,GPIO.LOW)
                            GPIO.output(11,GPIO.LOW)
                            GPIO.output(15,GPIO.LOW)
                            GPIO.output(19,GPIO.HIGH)
                            flagb=1
                            time.sleep(22)
                            #GPIO.output(11,GPIO.LOW)
                        
                    else:
                        GPIO.output(19,GPIO.LOW)
                
                except:

                    pass
            
            try:

                # mass center

                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


                # process every frame

                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)

                cv2.circle(frame, center, 5, (255, 0, 0), -1)

                

                # Forward and backward rule

                #if radius < 99:

                GPIO.output(15,GPIO.HIGH)    #forward
                #time.sleep(0.5)
                
                #elif radius > 100:

                   #motor.backward()

                 #else:

                   #motor.stop()
                   #GPIO.cleanup()
                    #GPIO.output(7,GPIO.LOW)


                # turn right and turn left rule
                #dist=get_distance()
                #print(dist)
                #print("moveforward")
               
                #if dist<40:#cm_ultrasonic wave turn into forward mode
                    ##GPIO.output(15,GPIO.LOW)
                    #GPIO.output(19,GPIO.HIGH)
                    #print("slightright")          
                if center[0] > Frame_Width/2 + 10:#turnRight
                    flag1=flag1+1
                    if(flag2>=20):  
                        GPIO.output(15,GPIO.LOW)
                        GPIO.output(11,GPIO.HIGH)
                    #time.sleep(1)
                    #GPIO.output(11,GPIO.LOW)
                        print("turnright")
                elif center[0] < Frame_Width/2 - 10:#turnLeft
                    flag2=flag2+1
                    if(flag2>=20):                        
                        GPIO.output(15,GPIO.LOW)
                        GPIO.output(13,GPIO.HIGH)
                    #time.sleep(1)
                    #GPIO.output(13,GPIO.LOW)
                        print("turnleft")
                 
        
                     
                else:
                    #motor.stop()
                    #GPIO.cleanup()
                    GPIO.output(13,GPIO.LOW)
                    GPIO.output(11,GPIO.LOW)
                    #GPIO.output(19,GPIO.LOW)
            # if not find mass center

            except:

                pass





        # mark these lines below if you don't need to display and the car will get faster

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1) & 0xFF



        if key == ord("q"):

            break

        # mark these lines above if you don't need to display and the car will get faster



finally:

        GPIO.cleanup()

        camera.release()

        cv2.destroyAllWindows()
