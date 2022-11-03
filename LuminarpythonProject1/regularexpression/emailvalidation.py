import re
rule='[\w_]+[@][g][m][a][i][l][.][c][o][m]'
f=open('mail.txt','r')
for i in f:
    s=i.rstrip('\n')
    #print(s)
    match=re.fullmatch(rule,s)
    if match is not None:
        print(s)
