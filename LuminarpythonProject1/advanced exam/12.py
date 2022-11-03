import re
def valid(func):
    def wrapper(a):
        rule = '[+][9][1]\d{10}'
        phn = re.fullmatch(rule,a)
        if phn is not None:
            return func(a)
        else:
            raise Exception("error in age")

    return wrapper

@valid
def change_number(phn_number):
    new_number=phn_number
    return new_number
phone=int(input("enter your phone"))
print(change_number(phone))