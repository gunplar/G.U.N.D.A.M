import evdev, select
import rospy
from diagnostic_msgs.msg import KeyValue
#from sensor_msgs.msg import Joy

if __name__=="__main__":

   pub = rospy.Publisher('control_signal', KeyValue, queue_size=100)
   rospy.init_node('controll_receiver')
   device = evdev.InputDevice('/dev/input/event0') #TODO: make variable
   try:
       publishData = KeyValue()
       while not rospy.is_shutdown():
            r, _, _ = select.select([device.fd], [], [], 0.05)
            if r:
                for event in device.read():
                   if event.type != 0:
                        publishData.key = str(event.code)
                        publishData.value = str(event.value)
                        pub.publish(publishData)
   except Exception as e:
       print(e)
