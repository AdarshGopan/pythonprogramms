name="adarsh gopan"
transation="TRANSACTION"
withdraw="WITHDRAW"
accountbal="ACCOUNTBALANCE"
changepin="CHANGEPIN"
pin="7034"
amount=20000
bank="dhanalakshmi bank"
print("PLEASE INSERT YOUR ATM CARD")
print("PROCESSING PLEASE WAIT.................")
op=input("SELECT OPTION\n TRANSACTION\nWITHDRAW\nACCOUNT BALANCE\nCHANGE PIN\n")
if op==transation:
    print("TRANSACTION SUCESSFULLY")
elif op==withdraw:
    upin=input("ENTER YOUR PIN NUMBER")
    if upin==pin:
        uamount=int(input("ENTER THE AMOUNT TO WITHDRAW"))
        if uamount<amount:
            print("WITHDRAW SUCESSFULLY\n")
            camount=amount-uamount
            print("YOUR CURRENT ACCOUNT BALANCE IS ",camount)
        else:
            print("INSUFFICIENT BALANCE")
    else:
        Print("WRONG PIN")
elif op==accountbal:
    print("YOUR ACCOUNT BALANCE IS",camount)
elif op==changepin:
    newpin=input("ENTER YOUR NEW PIN")
    pin=newpin
    print("CHANGED YOUR PIN SUCESSFULLY")
else:
    print("WRONG INPUT")