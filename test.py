import termios,sys,select,tty
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(350, 2250)
kit.servo[0].angle = 90
settings = termios.tcgetattr(sys.stdin)
while(1):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], None)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    if key == 'f' and kit.servo[0].angle<180:
        print(min(kit.servo[0].angle+3,180))
        kit.servo[0].angle = min(kit.servo[0].angle+3,180)
    elif key == 'j' and kit.servo[0].angle>0:
        print(max(kit.servo[0].angle-3,0))
        kit.servo[0].angle = max(kit.servo[0].angle-3,0)
    elif key == 'q':
        kit.servo[0].angle = None
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        break
    else: kit.servo[0].angle = None
