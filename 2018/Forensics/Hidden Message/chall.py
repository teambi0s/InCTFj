import string
import base64


def encode(x):
    return x.encode("hex") 

if __name__=="__main__":
	print("63486c306147397561584e6d6457343d")
	print("decode this to get the pass")
	encoded_data = encode(base64.b64encode(""))
	print(encoded_data)
