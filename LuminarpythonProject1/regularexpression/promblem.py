import re
rule='[\d\W]{1,5}' #{5}  #maximumlenght 5 with special charaters and numbers
v=input("enter your string:")
matcher=re.fullmatch(rule,v)
if matcher is not None:
    print("valid")
else:
    print("invalid")