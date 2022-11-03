import re
rule='[0-9]{10}'
phone=input("enter your number")
matcher=re.fullmatch(rule,phone)
if matcher is not None:
    print("valid")
else:
    print("not valid")