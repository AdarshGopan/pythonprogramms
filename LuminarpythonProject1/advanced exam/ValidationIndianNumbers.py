import re
f=open('phonenumber.txt','r')
f1=open('validindiannumber','w')
rule='[+][9][1]\d{10}'
for i in f:
    a=i.rstrip('\n')
    phn=re.fullmatch(rule,a)
    if phn is not None:
        f1.write(i)


