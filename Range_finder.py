# coding: utf-8
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGECHO = 15
GPIO_LED = 17

print ("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)  # Initial state as output
# Set trigger to False (Low)
GPIO.output(GPIO_TRIGECHO, False)
#setup LED output
GPIO.setup(GPIO_LED, GPIO.OUT)
#set it to off
GPIO.output(GPIO_LED, False)


def measure():
  # This function measures a distance
  # Pulse the trigger/echo line to initiate a measurement
    GPIO.output(GPIO_TRIGECHO, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGECHO, False)
  #ensure start time is set in case of very quick return
    start = time.time()

  # set line to input to check for start of echo response
    GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
    while GPIO.input(GPIO_TRIGECHO)==0:
        start = time.time()

  # Wait for end of echo response
    while GPIO.input(GPIO_TRIGECHO)==1:
        stop = time.time()
  
    GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
    GPIO.output(GPIO_TRIGECHO, False)

    elapsed = stop-start
    distance = (elapsed * 34300)/2.0
    time.sleep(0.1)
    return distance

def Flash_LED(distance):
    if distance < 30 and distance > 25:
        GPIO.output(GPIO_LED, True)
        time.sleep(2)
        GPIO.output(GPIO_LED, False)
        print("Distance is betweeen 25cm and 30cm")
        print("Drive forward")
    elif distance < 25 and distance > 18:
        GPIO.output(GPIO_LED, True)
        time.sleep(1)
        GPIO.output(GPIO_LED, False)
        print("Distance is between 18cm and 25cm")
        print("Slow down obstacle ahead")
    elif distance < 18:
        GPIO.output(GPIO_LED, True)
        time.sleep(0.1)
        GPIO.output(GPIO_LED, False)
        print("Distance is less than 18cm")
        print("Stop! Obstacle ahead")
        print("look around (left then right)")
    else:
        GPIO.output(GPIO_LED, False)
        print("Distance is greater than 30cm")
        print("Drive forward")

    


try:

    while True:

        distance = measure()
        print ("  Distance : %.1f cm" % distance)
        print ("\n")
        time.sleep(0.1)
        Flash_LED(distance)

except KeyboardInterrupt:
    print("Stop")
    GPIO.cleanup()