'''
Collection of functions used for the AutoHome project.

Author: Mohammad Odeh
Created: Jan 1st, 2017
'''

#import modules
import datetime
#import bluetooth

# Print full date and time
def timeStamp():
    days=["Mon.","Tues.","Wed.","Thurs.","Fri.","Sat.","Sun."]

    now = datetime.datetime.now()
    dayNumber=datetime.date(now.year, now.month, now.day).weekday()
    
    print (now.strftime("%a. %b %d, %Y %H:%M:%S"))


# Port Bind
#   This function binds the specified bluetooth device to a rfcomm port
#   Input   ::  {string} port type, {int} port number, {string} bluetooth address of device
#   Output  ::  None -- Terminal messages
def portBind(portType, portNumber, deviceBTAddress):
    print fullStamp() + " Connecting device to " + portType + str(portNumber)                    # Terminal message, program status
    os.system("sudo " + portType + " bind /dev/" + portType + str(portNumber) + " " + deviceBTAddress)     # Bind bluetooth device to control system

# Port Release
#   This function releases the specified communication port (serial) given the type and the number
#   Input   ::  {string} "portType", {int} "portNumber"
#   Output  ::  None -- Terminal messages
def portRelease(portType, portNumber):
    print fullStamp() + " Releasing " + portType + str(portNumber)                               # Terminal message, program status
    os.system("sudo " + portType + " release " + str(portNumber))                           # Releasing port through terminal commands


'''
# Send messages to a sever over Bluetooth using PyBluez
def connectToClient():
	serverMACAddress = 'B8:27:EB:D9:B4:0D'		# RPi BT address
	port = 0									# Arbitrary port
	s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	s.connect((serverMACAddress, port))
	while 1:
	    text = input()
	    if text == "quit":
	    	break
	    s.send(text)
	sock.close()


def connectToServer():
	hostMACAddress = 'B8:27:EB:D9:B4:0D' # The MAC address of the BT adapter on the server
	port = 3
	backlog = 1
	size = 1024
	s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	s.bind((hostMACAddress, port))
	s.listen(backlog)
	try:
	    client, clientInfo = s.accept()
	    while 1:
	        data = client.recv(size)
	        if data:
	            print(data)
	            client.send(data) # Echo back to client
	except:	
	    print("Closing socket")
	    client.close()
	    s.close()

####################################################################
#							EXPERIMENTAL						   #
####################################################################
def makeByte(data):
# write_port("06 10 46 46")
	dataB = []
	data = data.split(' ')
	print (data)
	for i in range(len(data)):
		dataB.insert(i,int(data[i],16))
	print( "".join(chr(i) for i in dataB) )

def write_port(*data):  # write_port(6, 10, 46, 46)
    dataB = []
    for i in range(len(data)):
        dataB.insert(i,int(data[i],16))
    ser.write( "".join(chr(i) for i in dataB) )

'''
