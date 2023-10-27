# find discount 

price = int(input("Enter price: "))
qty = int(input("Enter quantity: "))
amt = price*qty
if amt>1000:
    print("10% discount applicable")
    discount=amt*10/100
    amt=amt-discount
else:
    print("5% discount applicable")
    discount=amt*5/100
    amt=amt-discount
print("amount payable:",amt)
