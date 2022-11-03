fixed_amount=100000
need=int(input("enter the amount to withdraw"))
if fixed_amount >= need :
  print("withdraw successfully")
  fixed_amount=fixed_amount - need
  print("your account balance is", fixed_amount)
else:
    print("insufficient balance")
