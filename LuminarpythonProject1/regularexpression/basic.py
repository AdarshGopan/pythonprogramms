# regular expression
# pattern matching
import re
s=re.finditer('ab','abbabbabbaabbbbbaaaab')
count=0
for i in s:
    count+=1
    print(i.start())
    print(i.group())
print(count)