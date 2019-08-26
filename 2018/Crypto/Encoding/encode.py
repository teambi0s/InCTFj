
from secret import flag

for i in range(5):
	flag= flag.encode('base64')
	flag=flag.encode('hex')
f = open('ciphertext.txt','wb')
f.write(flag)
