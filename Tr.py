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

date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

buzzer=5

GPIO.setup(buzzer, GPIO.OUT)
control_pins = [4, 27, 10, 9]

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

MATRIX = [ [1,2,3,'A'],
           [4,5,6,'B'],
           [7,8,9,'C'],
           ['*',0,'#','D']]


ROW = [21,20,16,12] #negres
COL = [26,19,13,6] #blancs #18,23,24,25]
numeroentrat=''


def Funcmessage (textmessage):
    # Print a two line message
    lcd.clear()
    lcd.message(textmessage)

def Funcshowcursor ():
    # Demo showing the cursor.
    lcd.clear()
    lcd.show_cursor(True)
    lcd.message('Show cursor')

def Funcblink (textBlink):
    # Demo showing the blinking cursor.
    lcd.clear()
    lcd.blink(True)
    lcd.message(textBlink)

def Funcstopblink ():
    # Stop blinking and showing cursor.
    lcd.show_cursor(False)
    lcd.blink(False)

def FuncScroll(textScroll):   
    # Demo scrolling message right/left.
    lcd.clear()
    message = textScroll
    lcd.message(message)
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
        lcd.move_right()
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
        lcd.move_left()
def FuncSteppermotor (numero ):
    for i in range(numero*512/360): #512 una volta
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
    GPIO.cleanup()

def Funcnumpad ():
    for j in range(4):
        #print [j]
        #print COL[j]

        GPIO.setup(COL[j], GPIO.OUT)
        GPIO.output(COL[j],1)

        

    for i in range(4):
        GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
    try:
            while(True):
              if numeroentrat == '1122':
                Funcmessage ('codi correcte');
                FuncSteppermotor (360);
                #lcd.clear();

              if numeroentrat == '1727':
                Funcmessage ('codi correcte');
                #lcd.clear();
              for j in range(4):
                    GPIO.output(COL[j],0)
                    for i in range(4):
                        if GPIO.input(ROW[i]) == 0:
                            print (MATRIX[i] [j])
                            global numeroentrat
                            if (MATRIX[i] [j]) == 'C':
                              numeroentrat = ''
                              #lcd.clear()
                            else :
                              numeroentrat = numeroentrat + str(MATRIX[i] [j])
                              Funcmessage ('Has premut ' + numeroentrat)
                              time.sleep(0.2)

                            while(GPIO.input(ROW[i]) == 0):
                                pass

                    GPIO.output(COL[j],1)
    except KeyboardInterrupt:
            GPIO.cleanup()

                            
def FuncCamara ():

###camera.start_preview()
###s#leep(10)
    print('/home/pi/Desktop/image'+date_string+'.jpg')
    camera.capture('/home/pi/Desktop/image'+date_string+'.jpg')
    camera.stop_preview()
    sleep(3600)
 
    
   

FuncScroll ('Hola');
Funcblink ('Escriu codi');
Funcnumpad();
#FuncCamara();
