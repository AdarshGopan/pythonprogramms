import re
s=re.finditer('[A-Z][a-z\W]+', "AgjnA#@AAAGBgjn")
count=0
for i in s:
    count=count+1
    print( i.start() )
    print(i.group())
print(count)