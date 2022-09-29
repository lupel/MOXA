

# 23-09-22 lupel

import can
import time
import os

board_id = 108

# Convert 16 bit signed into float
def convert_temp(a):
	t = 0
	if(a & 0x8000):			# Check negative value
		a = -0x10000 + a
	t = a *.25
			
	return t

print('\n\rCAN Rx test')
print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1)	

try:
	bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
	print('Cannot find PiCAN board.')
	exit()
	
print('Ready')

try:
	while True:
		message = bus.recv()	# Wait until a message is received.

		s=''
		for i in range(message.dlc ):
			s +=  '{0:x} '.format(message.data[i])
			
		if message.arbitration_id == board_id:	# Check CAN ID is for this board
			p1 = 0
			p2 = 0
			if(message.data[2] == 0):			# Check Probe 1 status
				p1_stat = "Probe 1 OK"
				p1 = convert_temp((message.data[0]) | (message.data[1] <<8))
			else:
				p1_stat = "Probe 1 Fault"
			
			if(message.data[6] == 0):			# Check Probe 2 status
				p2_stat = "Probe 2 OK"
				p2 = convert_temp((message.data[4]) | (message.data[5] <<8))
			else:
				p2_stat = "Probe 2 Fault"			
			
			#print(' {} '.format(s))
			print('{} {} degree C     {} {} degree C'.format(p1_stat,p1,p2_stat,p2))
	
except KeyboardInterrupt:
	#Catch keyboard interrupt
	os.system("sudo /sbin/ip link set can0 down")
	print('\n\rKeyboard interrtupt')	
