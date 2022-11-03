import re
rule='[A-Za-z0-9]@'
v=input("enter your gmail:")
matcher=re.fullmatch(rule,v)
if matcher is not None:
    print("valid")
else:
    print("not valid")