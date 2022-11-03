import re
rule='^a' #'[^abc]','[abc]','[a-z]','[A-Z]','[A-Za-z]','[^A-za-z]','[^12]'=>1 or 2 not 12
s=re.finditer(rule,'aaa aaaaa abc cb zz @123abABC') #abc abcaaFgh@G4 d
count=0
for i in s:
    count+=1
    print(i.start())
    print(i.group())
print(count)