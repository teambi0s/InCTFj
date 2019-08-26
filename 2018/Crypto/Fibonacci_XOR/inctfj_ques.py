from inctfj import message,k,n

def fibonacci(n):
	ar = []
	a,b = 1,1
	ar.append(a)
	ar.append(b)
	for i in range(n-2):
		c = a + b
		ar.append(c)
		a = b
		b = c	
	return ar

def keygeneration(k):
	assert len(k) == 4
	key = ""
	ar = fibonacci(n)
	for i in range(len(ar)):
		key = key + k[i%len(k)]*ar[i]
	return key

def encryption(message):
	assert len(message) == sum(fibonacci(n))
	ct = ""
	for i in range(len(message)):
		ct = ct + chr(ord(message[i]) ^ ord(key[i]))
	return ct.encode("hex")

key = keygeneration(k)
ciphertext = encryption(message)
f = open('ciphertext.txt','w').write(ciphertext)

