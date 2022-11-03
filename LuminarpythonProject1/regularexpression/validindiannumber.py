import re
rule='[+][9][1][0-9]{10}'
v=open('validenumber.txt','w')
f=open('phonenumber.txt','r')
for i in f:
    phn=i.rstrip("\n")
    match=re.fullmatch(rule,phn)
    if match is not None:
        v.write(i)

