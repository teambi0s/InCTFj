### Chall Name
s3cur3PHP

### Chall Difficulty
5/5

### Chall Description
I think that this PHP code is highly s3cur3, do you think otherwise?

### Chall Link
http://35.154.254.85/s3cur3PHP/

### Chall Flag
inctfj{!_d0n7_kn0w_4b0u7_y0u_bu7_PHP_!5_s0_d4mn_c00l}

### Chall Author
c3rb3ru5

### Chall Solution
On the landing page is a base64 encoded message, which on decoding gives a python commnand which on running gives "send get request using viewsource parameter". On using the viewsource parameter, we are able to view the PHP Code. And then there are a few checks to bypass. The final URL for the flag is:

```
http://35.154.254.85/s3cur3PHP/?viewsource&flag[]&secret=1729aaaaaaaaa
```

The flag is there in the source code.
