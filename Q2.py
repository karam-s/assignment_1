while 1:
    decimal_num = int(input("enter a decimal numbe: "))
    pout=decimal_num
    if decimal_num==-1:
        break
    
    binary_num = []
    while decimal_num!=0:
        y= decimal_num %2
        binary_num.append(y)
        decimal_num=decimal_num//2
        
    binary_num.reverse()
    print ("the binary number of the "+str(pout)+" \
is: "+"".join([str(i) for i in binary_num]))
    print ("to break the loop enter -1")
    
