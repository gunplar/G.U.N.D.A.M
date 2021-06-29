# G.U.N.D.A.M
ROS package for hobby humanoid robot


## Settup

Flash Dietpi (32 bit) onto the SD card 
Set the wifi connection in the text file
Connect with SSH
Enable bluetooth on first bootup or later through `dietpi-config`
Install python3 and pip3

### Bluetooth

Disable ERTM so Pi can pair with the XBOX One controller
`echo 'options bluetooth disable_ertm=Y' | sudo tee -a /etc/modprobe.d/bluetooth.conf`

  `bluetoothctl
  power on
  scan on
  connect <MAC address here>
  trust <MAC address here>`
