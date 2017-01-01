'''
Collection of functions used for the AutoHome project.

Author: Mohammad Odeh
Created: Jan 1st, 2017
'''

#import modules
import datetime

# Print full date and time
def timeStamp():
    days=["Mon.","Tues.","Wed.","Thurs.","Fri.","Sat.","Sun."]

    now = datetime.datetime.now()
    dayNumber=datetime.date(now.year, now.month, now.day).weekday()
    
    print (now.strftime("%a. %b %d, %Y %H:%M:%S"))


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
