# G.U.N.D.A.M
ROS package for hobby humanoid robot


## Settup

Flash Dietpi (32 bit) onto the SD card 

Set the wifi connection in the text file

Accept the license in dietpi.txt

Connect with SSH

Enable bluetooth on first bootup or later through `dietpi-config`

Install python3 and pip3

pip3 install adafruit-circuitpython-servokit

### Bluetooth

Disable ERTM so Pi can pair with the XBOX One controller. Refer to [this article](https://howchoo.com/pi/xbox-controller-raspberry-pi) for more information

> echo 'options bluetooth disable_ertm=Y' | sudo tee -a /etc/modprobe.d/bluetooth.conf

  `bluetoothctl
  power on
  scan on
  connect <MAC address here>
  trust <MAC address here>`

To revert to stable version: https://www.raspberrypi.org/forums/viewtopic.php?t=268915
If `No default controller available` in bluetoothctl, install `pi-bluetooth`, use `modprobe bluetooth` and `systemctl start bluetooth`
