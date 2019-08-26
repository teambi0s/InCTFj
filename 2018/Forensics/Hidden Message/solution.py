import string
import base64


def encode(x):
    return x.decode("hex") 

if __name__=="__main__":
	print("63486c306147397561584e6d6457343d")
	print("decode this to get the pass")
	encoded_data = base64.b64decode(encode("63486c306147397561584e6d6457343d"))
	print(encoded_data)
