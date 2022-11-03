s={12,-254,-84,-95,55,99,-288,9,-1,-3,6,0}
print("orginal set=  ",s)
pos=set()
neg=set()
for i in s:
    if i>=0:
        pos.add(i)
    else:
        neg.add(i)
print("positive set=",pos)
print("negative set=",neg)
