from inctfj_ques import fibonacci, keygeneration
from sets import Set
import string

def series_length(ciphertext):
	for i in range(13): #some random length to find n
		f = fibonacci(i)
		if len(ciphertext) == sum(f):
			return i

def arrangement(ciphertext):
	lists = [[] for _ in range(0,4)]
	k = 0
	for i in range(n):
		for j in range(ar[i]):
			lists[i%4].append(ciphertext[k])
			k = k + 1
	return lists

def key():
	lists = arrangement(ciphertext)
	b = Set(string.letters + " " + string.digits + "!" + "." + "?" + "{" + "}" + "_")
	s1 = ""
	for r in range(0,4):	
		for k in range(96,125):
			p = ""
			for t in range(0,len(lists[r])):
				p = p + chr(ord(lists[r][t]) ^ ord(chr(k)))			
			if all(c in b for c in p):
				s1 = s1 + chr(k)
				break		
	return s1

def decryption(ciphertext):
	pt = ""
	for i in range(len(ciphertext)):
		pt = pt + chr(ord(ciphertext[i]) ^ ord(key[i]))
	return pt

ciphertext = "010f00170d011059375f0058140609563e50153e1457103c1050001611503c0b531c340f5a0f34125b1e340919585f00345a1f54164b31581d48091a5b4809480f5b06591d1b494831581d480c590c4809480f1a5b091c480b510340412952551315184102510f06130056140d005650510f1241510f4112510d17080f064115095012410209550d0d520f06524040".decode("hex")
n = series_length(ciphertext)
ar = fibonacci(n)
ciphertext = list(ciphertext)
key = key()
key = keygeneration(key)
plaintext = decryption(ciphertext)
print plaintext
