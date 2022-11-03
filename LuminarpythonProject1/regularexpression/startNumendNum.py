import re
rule='^\d[\d\W]{4}\d$'   #[a][A-za-z0-9]{1,}[b]
v=input("enter your string:")
matcher=re.fullmatch(rule,v)
if matcher is not None:
    print("valid")
else:
    print("not valid")