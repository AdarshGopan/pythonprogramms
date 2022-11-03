import re
rule='^[A-z][\w]{3,8}[A-Z]$'
n=input('enter the string')
a=re.fullmatch(rule,n)
if a is not None:
    print("valid")
else:
    print("invalid")