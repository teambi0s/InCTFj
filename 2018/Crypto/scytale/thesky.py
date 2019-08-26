#This is the encryption pattern used for Tale of the Sky
import random

def encrypt():
	print "Enter the message: "
	message=raw_input()
	turns = random.randrange(3,13);
	ct=""
	for i in range(turns):
		for j in range(0,len(message)-i,turns):
			ct+=message[i+j]
	print turns
	print "[+]"+message
	print "[#]"+ct

encrypt()

