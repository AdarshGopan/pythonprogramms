# decorators
def valuecheck(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return wrapper
@valuecheck
def sub(n1,n2):
    return n1-n2
print(sub(7,9))

@valuecheck
def div(n1,n2):
    return n1/n2
print(div(2,8))