 def valuecheck(func):
    def wrapper(a,b):
        if a=='admin':
            return func(a,b)
        else:
            raise Exception("error in user")
    return wrapper

@valuecheck
def vaccinecheck(u,pin):
    return pin
u=input("enter your type")
pin=int(input("enter your pin"))
print(vaccinecheck(u,pin))