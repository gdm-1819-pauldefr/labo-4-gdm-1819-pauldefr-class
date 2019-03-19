import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def trafic():
  GPIO.setup(18,GPIO.OUT)
  print "LED on"
  GPIO.output(18,GPIO.LOW)

  GPIO.setup(24,GPIO.OUT)
  GPIO.setup(7,GPIO.OUT)
  print "LED off"
  GPIO.output(24,GPIO.HIGH)
  GPIO.output(7,GPIO.HIGH)

  time.sleep(2)

  GPIO.setup(7,GPIO.OUT)
  print "LED on"
  GPIO.output(7,GPIO.LOW)

  GPIO.setup(24,GPIO.OUT)
  GPIO.setup(18,GPIO.OUT)
  print "LED off"
  GPIO.output(24,GPIO.HIGH)
  GPIO.output(18,GPIO.HIGH)

  time.sleep(2)

  GPIO.setup(24,GPIO.OUT)
  print "LED on"
  GPIO.output(24,GPIO.LOW)

  GPIO.setup(7,GPIO.OUT)
  GPIO.setup(18,GPIO.OUT)
  print "LED off"
  GPIO.output(7,GPIO.HIGH)
  GPIO.output(18,GPIO.HIGH)

  trafic()

trafic()
