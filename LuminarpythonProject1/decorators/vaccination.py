def valuecheck(func):
    def wrapper(a,b):
        if b<18:
            raise Exception("error in age")
        else:
            return func(a,b)
    return wrapper

@valuecheck
def vaccinecheck(name,age):
    return "vaccinatted sucessfully"
age=int(input("enter your age"))
print(vaccinecheck("adarsh",age))