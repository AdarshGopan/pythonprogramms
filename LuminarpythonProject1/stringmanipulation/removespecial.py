n=input("enter the text")
s='''!@#$%^&*()[]\|?/`''""~{}:<>,.;+=-:123456789'''
m=""
for i in n:
    if i not in s:
        m=m+i
print(m)