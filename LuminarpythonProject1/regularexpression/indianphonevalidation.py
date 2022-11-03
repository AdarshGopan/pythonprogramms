import re
rule='[+][9][1][0-9]{10}'
v=input("enter your number")
matcher=re.fullmatch(rule,v)
if matcher is not None:
    print("numner is valid")
else:
    print("number is not valid")