import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1) # or smbus.SMBus(0)

# ISL29125 address, 0x44(68)
# Select configuation-1register, 0x01(01)
# 0x0D(13) Operation: RGB, Range: 360 lux, Res: 16 Bits
bus.write_byte_data(0x44, 0x01, 0x05)

time.sleep(1)

print("Reading colour values and displaying them in a new window\n")

def getAndUpdateColour():
    while True:
	# Read the data from the sensor
        # Insert code here
        data = bus.read_i2c_block_data(0x44, 0x09, 6)

        # Convert the data to green, red and blue int values
        # Insert code here

        

    
        green = data[1] + data[0]/256
        red = data[3] + data[2]/256
        blue = data[5] + data[4]/256

        total = green + red + blue

        red = red/total
        green = green/total
        blue = blue/total

        green = green/ 1.5
        blue = blue * 1.6

        #green = green *2
        if red > green and red > blue:
            print("Red: ", red)
        elif green > red and green > blue:
            print("Green: ", green)
        elif blue > red and blue > green:
            print("Blue: ", blue)

        
        print("RGB = %lf, %lf, %lf" % (red, green, blue))
             # Output data to the console RGB values
        # Uncomment the line below when you have read the red, green and blue values
        # print("RGB(%d %d %d)" % (red, green, blue))
        print()
        
        time.sleep(2) 

getAndUpdateColour()
