#KL10TR2455
import re
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
v=input("enter your vehicle number")
matcher=re.fullmatch(rule,v)
if matcher is not None:
    print("valid")
else:
    print("not valid")