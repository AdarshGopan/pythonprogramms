import re
rule='[L][U][M][p][y]\d{4}'
f=open('reg.txt','r')
f1=open('python.txt','w')
f2=open('datascience.txt','w')
for i in f:
    reg=i.rstrip('\n')
    match=re.fullmatch(rule,reg)
    if match is not None:
        f1.write(i)
    else:
        f2.write(i)