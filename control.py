from adafruit_servokit import ServoKit
import time, threading, termios, sys, select, tty

kit = ServoKit(channels=16)
controlKeyPressed = ''

class servoThread (threading.Thread):
   global controlKeyPressed
   def __init__(self, servoID, initAngle, angleUpKey, angleDownKey):#, threadQuitKey):
       super().__init__()
       self.servoID = servoID
       self.angleUpKey = angleUpKey
       self.angleDownKey = angleDownKey
       self.currentAngle = initAngle
       #self.threadQuitKey=threadQuitKey
       kit.servo[servoID].actuation_range = 180
       kit.servo[servoID].set_pulse_width_range(350, 2250)
       kit.servo[servoID].angle = initAngle
       self.start()
   def run(self):
       while(1):
         if controlKeyPressed == self.angleUpKey and self.currentAngle<180:
             self.currentAngle = min(self.currentAngle + 4, 180)
             kit.servo[self.servoID].angle = self.currentAngle
             time.sleep(0.05)
             kit.servo[self.servoID].angle = None
         elif controlKeyPressed == self.angleDownKey and self.currentAngle>0:
             self.currentAngle = max(self.currentAngle - 4, 0)
             kit.servo[self.servoID].angle = self.currentAngle
             time.sleep(0.05)
             kit.servo[self.servoID].angle = None
         #elif controlKeyPressed == self.threadQuitKey:
         #    kit.servo[self.servoID].angle = None
         #    print("Thread exit",self.servoID)
         #    #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
         #    break

if __name__=="__main__":
   settings = termios.tcgetattr(sys.stdin)
   thread1 = servoThread(0,90,'y','h')#,'p')
   thread2 = servoThread(1,90,'f','v')#,'q')
   tty.setcbreak(sys.stdin.fileno())
   try:
       while(1):
           #READING KEY IN MAIN THREAD
            rlist, _, _ = select.select([sys.stdin], [], [], 0.05)
            if rlist:
                controlKeyPressed = sys.stdin.read(1)
            else:
                controlKeyPressed = ''
   except Exception as e:
       print(e)
   finally:
       termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

