import requests,datetime
from gpiozero import MotionSensor
#from picamera import PiCamera
from signal import pause
from time import sleep

#camera = PiCamera()
pir = MotionSensor(17)

print("ALARM Starting")
sleep(10) #wait for the sensor to settle

def send_msg():
	timestamp = datetime.datetime.now()
	timestamp = str(timestamp.strfime("%Y-%m-%d %H:%M:%S)
	print("ALARM TRIGGERED: "+timestamp);
	#camera.capture("/home/pi/"+str(timestamp)+".jpg")
	r=requests.post(
		"https://api.pushover.net/1/messages.json", 
		data={
			"token":"abwzonx3o89y7depqejnjc3uwuvhg4",
			"user":"uuh2cufwr56y6kzxmzedgtrtbxzirm",
			"message":("Alert:"+timestamp)},
		files={
			"attachment":(timestamp,open("/home/pi/"+str(timestamp)+".jpg","rb"),"image/jpeg")}
	)
	
	print(r.text)
	sleep(30)
	
while True:
	pir.wait_for_motion()
	send_msg()
	pir.wait_for_no_motion()
	
#https://projects.raspberrypi.org/en/projects/physical-computing/13
#https://gpiozero.readthedocs.io/en/stable/api_input.html#motion-sensor-d-sun-pir
		
