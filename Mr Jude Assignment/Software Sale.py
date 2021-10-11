

userNumberOfPackages = int( input("please enter the number of packages bought: "))

packagePrice = 99


if userNumberOfPackages < 10:
    discount = 0;
    
elif userNumberOfPackages < 20:
    discount = .10
elif userNumberOfPackages <50:
    discount = .20
elif userNumberOfPackages <100:
    discount = .30
else:
    discount = .40
    

subTotal = userNumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount 

print ("Discount Amount @ " +format(discount,'.0%')+ ": " + "${:,.2f}".format(discountAmount,))
print ("Total Amount :" + "${:,.2f}".format(total))