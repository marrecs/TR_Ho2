#Treball Recerca H2o
#13-12-2018

#Importem llibreries
import time
import Adafruit_CharLCD as LCD
import sys
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

date_string = datetime.datetime.now().strftime("%Y-%m-&d-%H:%M")

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

buzzer=5

GPIO.setup(buzzer, GPIO.OUT)
control_pins = [4, 27, 10, 9]
numero = 360

# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
lcd.message('Hello\nworld!')

# Wait 5 seconds
time.sleep(5.0)

# Demo showing the cursor.
lcd.clear()
lcd.show_cursor(True)
lcd.message('Show cursor')

time.sleep(5.0)

# Demo showing the blinking cursor.
lcd.clear()
lcd.blink(True)
lcd.message('Blink cursor')

time.sleep(5.0)

# Stop blinking and showing cursor.
lcd.show_cursor(False)
lcd.blink(False)

# Demo scrolling message right/left.
lcd.clear()
message = 'Scroll'
lcd.message(message)
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()

# Demo turning backlight off and on.
lcd.clear()
lcd.message('Flash backlight\nin 5 seconds...')
time.sleep(5.0)
# Turn backlight off.
lcd.set_backlight(0)
time.sleep(2.0)
# Change message.
lcd.clear()
lcd.message('Goodbye!')
# Turn backlight on.
lcd.set_backlight(1)


MATRIX = [ [1,2,3,'A'],
           [4,5,6,'B'],
           [7,8,9,'C'],
           ['*',0,'#','D']]

#ROW = [7,11,13,15]
#COL = [12,16,18,22]

ROW = [21,20,16,12] #negres
COL = [26,19,13,6] #blancs #18,23,24,25] 

print ("Pas1")

for j in range(4):
    #print [j]
    #print COL[j]

    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j],1)

    

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #print [i]
    #print ROW[i]

try:
        while(True):
            for j in range(4):
                GPIO.output(COL[j],0)
                #print [j]
                #print "pas2"
                #print (MATRIX[i] [j])

                for i in range(4):
                    #print (MATRIX[i] [j])
                    #time.sleep(0.82)

                    #print i
                    #print "pas3"
                    if GPIO.input(ROW[i]) == 0:
                        print (MATRIX[i] [j])
                        lcd.clear()
                        if str(MATRIX[i] [j]) == "1":
                            lcd.message('Has premut ' + str(MATRIX[i] [j]))
## escriure el que el motor giri
##import RPi.GPIO as GPIO
##import time
##GPIO.setmode(GPIO.BCM)
##control_pins = [4,27,10,9]
##numero = 360
                            for pin in control_pins:
                              GPIO.setup(pin, GPIO.OUT)
                              GPIO.output(pin, 0)
                             halfstep_seq = [
                              [1,0,0,0],
                              [1,1,0,0],
                              [0,1,0,0],
                              [0,1,1,0],
                              [0,0,1,0],
                              [0,0,1,1],
                              [0,0,0,1],
                              [1,0,0,1]
                                    ]
                    for i in range(numero*512/360): #512 una volta
                        for halfstep in range(8):
                            for pin in range(4):
                              GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                            time.sleep(0.001)
                            GPIO.cleanup()


                    for temps in range(MATRIX[i] [j]):
                            GPIO.output(buzzer,GPIO.HIGH)
                            print('Beep')
                            time.sleep(0.5)
                            GPIO.output(buzzer,GPIO.LOW)
                            print('No Beep')
                            time.sleep(0.5)
                            time.sleep(0.2)
                   
##from picamera import PiCamera
##from time import sleep
##import datetime

##create object for PiCamera class
##camera = PiCamera()
#DateTime = str(datetime.datetime.now())

#DateTime.Now.ToString("yyyy-dd-M--HH-mm-ss");
##date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
#camera.start_preview()
#sleep(10)
                    
                    print('/home/pi/Desktop/image'+date_string+'.jpg')
                    camera.capture('/home/pi/Desktop/image'+date_string+'.jpg')
                    camera.stop_preview()
                    sleep (86400)
##   espera 24h                 
                    
                        

                 while(GPIO.input(ROW[i]) == 0):
                            pass


                        
                
                GPIO.output(COL[j],1)
except KeyboardInterrupt:
        GPIO.cleanup()

