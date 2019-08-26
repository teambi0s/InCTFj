import hashlib

opr=hashlib.md5()
op2=hashlib.sha256()
list1=[122,86,83,116,13,16,116,52,7,69,10,69,76,93,13,87]
print "\t-------------------------------------------\n"
print "\t | LIGHT UP THE FIRE- FIRE of REVOLUTION | \n"
print "\t-------------------------------------------\n"


ing1=raw_input("Fuel it up.Enter the key: ")
opr.update(ing1)

res1="m0st_impOrt4nt_one.!"
res1 = [chr(ord(a) ^ ord(b)) for a,b in zip(opr.hexdigest(),res1)]
res1="".join(res1)



ing2=raw_input("\n\t-------------------------------------------\n\nEnter the second key to intensify the fire : ")
opr.update(ing2)
res2="n0te_down_7he_secOnd_0ne1"	
res2 = [chr(ord(a) and ord(b)) for a,b in zip((opr.hexdigest())[::-1],res2)]
opr.update(str(res2))
res2 = [chr(ord(a) or ord(b)) for a,b in zip((opr.hexdigest()),res1)]
res2="".join(res2)
opr.update(str(res2))
if (opr.hexdigest()=="6848df0f43f084b97f4e6d987da093fb"):

	str1 = [chr(ord(a) ^ b) for a,b in zip((opr.hexdigest()),list1)]

	print "\n\t-------------------------------------------\n\nThe flag is: " +"inctfj{"+ "".join(str1) + "}\n "	
else :
	print "\n\nCome on! Bring in more spirit\n"
