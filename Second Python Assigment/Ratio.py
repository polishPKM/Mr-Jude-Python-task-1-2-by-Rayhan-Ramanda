def NHeight():
    cw = eval(input("Enter current width: "))
    ch = eval(input("Enter current height: "))
    dw = eval(input("Enter the desired width: "))
    while dw > cw:
        dw = eval(input("Desire width must be smaller than current width, please re-enter: "))
   
    a = cw / dw
    b = ch / a
    print("The corresponding height is: ", b)



NHeight()