'''
Communication protocol definitions used for the AutoHome project.

Author: Mohammad Odeh
Created: Jan 1st, 2017
'''

# Byte definition               DescriptionValue   	 	        Value
# ---------------		----------------		        -----

# General
# -------
SOH = b'\x01'  	#               Start Of Header			        0x01
EOT = b'\x04'	#		End of Transmission			0x04
ENQ = b'\x05'	#		Enquiry					0x05
ACK = b'\x06'	#		Acknowledgment				0x06
NAK = b'\x15'	#		Negative Acknowledgment		        0x15



# Device Control
# --------------
DC1 = b'\x11'	#		Device Control 1 (XON)		        0x11
DC2 = b'\x12'	#		Device Control 2			0x12
DC3 = b'\x13'	#		Device Control 3 (XOFF)		        0x13
DC4 = b'\x14'	#		Device Control 4			0x14
