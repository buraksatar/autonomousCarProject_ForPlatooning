sudo ifconfig wlan0 up
sleep 5

cd /
cd home/pi/Desktop/Transmitter
sudo python proximityToFirebase.py
cd /
