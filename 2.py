D_num=int(input("enter a decimal nimber: "))
B_num=[]
while D_num!=0:
    y= D_num % 2
    B_num.append(y)
    D_num= D_num // 2
B_num.reverse()
print("the binary number of the " + str(B_num))