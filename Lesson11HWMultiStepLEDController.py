import RPi.GPIO as GPIO
from time import sleep

debug = True

DutyCycle = 1.0
DutyCycleUpperLimit = 99.9
DutyCycleLowerLimit = 0.01
Steps = 8.0
LEDIncrement = (DutyCycleUpperLimit - DutyCycleLowerLimit) / Steps
Frequency = 100
RedBrightness = 0.1/1.0
GreenBrightness = 0.1/1.0
BlueBrightness = 0.1/1.0
RedIncrement = LEDIncrement
GreenIncrement = LEDIncrement
BlueIncrement = LEDIncrement

RedPin = 11
GreenPin = 13
BluePin = 37

RedSwitch = 16
GreenSwitch = 18
BlueSwitch = 22

RedButtonState = 0
RedButtonStateOld = 0
GreenButtonState = 0
GreenButtonStateOld = 0
BlueButtonState = 0
BlueButtonStateOld = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedPin, GPIO.OUT)
GPIO.setup(GreenPin, GPIO.OUT)
GPIO.setup(BluePin, GPIO.OUT)
RedPWM = GPIO.PWM(RedPin, Frequency)
GreenPWM = GPIO.PWM(GreenPin, Frequency)
BluePWM = GPIO.PWM(BluePin, Frequency)
GPIO.setup(RedSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GreenSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BlueSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

Delay = .1

try:
    while True:
        RedButtonState = GPIO.input(RedSwitch)
        if RedButtonState == 1 and RedButtonStateOld == 0:
            if RedBrightness >= DutyCycleUpperLimit or RedBrightness <= DutyCycleLowerLimit:
                    RedIncrement = RedIncrement * (-1)
            RedBrightness = RedBrightness + RedIncrement
            if RedBrightness >= float(100):
                RedBrightness = 99.99
            if RedBrightness <= 0.0:
                RedBrightness = 0.01
            RedPWM.start(RedBrightness)
        RedButtonStateOld = RedButtonState
        GreenButtonState = GPIO.input(GreenSwitch)
        if GreenButtonState == 1 and GreenButtonStateOld == 0:
            if GreenBrightness >= DutyCycleUpperLimit or GreenBrightness <= DutyCycleLowerLimit:
                    GreenIncrement = GreenIncrement * (-1)
            GreenBrightness = GreenBrightness + GreenIncrement
            if GreenBrightness >= float(100):
                GreenBrightness = 99.99
            if GreenBrightness <= 0.0:
                GreenBrightness = 0.01
            GreenPWM.start(GreenBrightness)
        GreenButtonStateOld = GreenButtonState
        BlueButtonState = GPIO.input(BlueSwitch)
        if BlueButtonState == 1 and BlueButtonStateOld == 0:
            if BlueBrightness >= DutyCycleUpperLimit or BlueBrightness <= DutyCycleLowerLimit:
                    BlueIncrement = BlueIncrement * (-1)
            BlueBrightness = BlueBrightness + BlueIncrement
            if BlueBrightness >= float(100):
                BlueBrightness = 99.99
            if BlueBrightness <= 0.0:
                BlueBrightness = 0.01
            BluePWM.start(BlueBrightness)
        BlueButtonStateOld = BlueButtonState

        if debug:
            print("RedBrightness= ", RedBrightness, 
                " GreenBrightness= ", GreenBrightness, 
                " BlueBrightness= ", BlueBrightness)
                
        sleep(Delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nGPIO is cleaned up.")

        
            
