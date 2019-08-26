from Crypto.Util.number import *
from secret import flag

p = getPrime(512)
q = getPrime(512)

#public key pair (n,e) generated
n = p*q
e = 65537

#
plaintext=flag

#python's in-built function to convert a character string to equivalent long decimal
message = bytes_to_long(plaintext)

#ciphertext calculated here
ciphertext=(message**e)%n

#You'll have to find what is flag when one of the generator prime p, public key (n,e) and ciphertext is given to you.
print( "Generator prime p :%d"%( plaintext ))
print( "Public key n:%d"%( n ))
print( "Public key e:%d"%( e )
print( "Ciphertext :%d"%( ciphertext ))



