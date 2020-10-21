# Executing Multiple statement

Price = float (input("Enter Price ?"))
Qty = float (input("Enter Qty ?"))

Amt = Price* Qty

print("Amount :" , Amt)

if Amt >3000:
    disc = Amt * .20
    print("Discount :-", disc)
elif Amt>1000:
    disc = Amt * .10
    print("Discount :-", disc)
else:
    disc = Amt * .05
    print("Discount :-", disc)