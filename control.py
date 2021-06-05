from adafruit_servokit import ServoKit
import time, threading, termios, sys, select, tty

kit = ServoKit(channels=16)

class servoThread (threading.Thread):
   def __init__(self, servoID, initAngle, angleUpKey, angleDownKey, threadQuitKey):
       super().__init__()
       self.servoID=servoID
       self.angleUpKey=angleUpKey
       self.angleDownKey=angleDownKey
       self.threadQuitKey=threadQuitKey
       kit.servo[servoID].actuation_range = 180
       kit.servo[servoID].set_pulse_width_range(350, 2250)
       kit.servo[servoID].angle = initAngle
       self.start()
   def run(self):
      while(1):
         tty.setraw(sys.stdin.fileno())
         rlist, _, _ = select.select([sys.stdin], [], [], None)
         if rlist:
             key = sys.stdin.read(1)
         else:
             key = ''
         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
         if key == self.angleUpKey and kit.servo[self.servoID].angle<180:
             print(min(kit.servo[self.servoID].angle+4,180))
             kit.servo[self.servoID].angle = min(kit.servo[self.servoID].angle+4,180)
         elif key == self.angleDownKey and kit.servo[self.servoID].angle>0:
             print(max(kit.servo[self.servoID].angle-4,0))
             kit.servo[self.servoID].angle = max(kit.servo[self.servoID].angle-4,0)
         elif key == self.threadQuitKey:
             kit.servo[self.servoID].angle = None
             print("Thread exit",self.servoID)
             #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
             break

if __name__=="__main__":
   settings = termios.tcgetattr(sys.stdin)
   thread1 = servoThread(0,90,'i','k','p')
   thread2 = servoThread(1,90,'e','d','q')

