import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

##BUTTON##
btn1 = 21
btn2 = 20
btn3 = 16
btn4 = 26
btn5 = 19
btn6 = 13
btn7 = 6
btn8 = 5
##!!BUTTON##

GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.OUT)

GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(4,50)

##LCD CONFIG
lcd_rs        = 25 
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
##!!LCD CONFIG##

def pushingBtn():
    if GPIO.input(btn1):
        return 1
    elif GPIO.input(btn2):
        return 2
    elif GPIO.input(btn3):
        return 3
    elif GPIO.input(btn4):
        return 4
    elif GPIO.input(btn5):
        return 5
    elif GPIO.input(btn6):
        return 6
    elif GPIO.input(btn7):
        return 7
    elif GPIO.input(btn8):
        return 8
    else: 
        return 0

#lcd.clear()
  #p.ChangeDutyCycle(7.5) 
  #lcd.message('90 derece...')
  #time.sleep(2)
  #lcd.clear()
  #p.ChangeDutyCycle(12.5) 
  #lcd.message('180 derece...')
  #time.sleep(2)
  #lcd.clear()
  #p.ChangeDutyCycle(2.5) 
  #lcd.message('0 derece...')
  #time.sleep(2)

p.start(12.5)
sifre = ''
gercekSifre = ''
lcd.message('Enter pass:\n'+sifre)
try:
 while True:
  if len(sifre) >= 4:
      lcd.clear()
      if gercekSifre == '1234':
        
       lcd.message('Access accepted!!')
       p.ChangeDutyCycle(2.5) 
       time.sleep(5)
       sifre = ''
       p.ChangeDutyCycle(12.5) 
       lcd.clear()
       lcd.message('Enter pass:\n'+sifre)
      else: 
       lcd.message('Access denied!!')
       time.sleep(5)
       sifre = ''
       lcd.clear()
       lcd.message('Enter pass:\n'+sifre)

  else:
      gelen = pushingBtn()
      if gelen != 0:
       sifre += '*'
       gercekSifre = ''.join([gercekSifre, str(gelen)])
       print(gelen)
       lcd.clear()
       lcd.message('Enter pass:\n'+sifre)
       time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
  p.stop()