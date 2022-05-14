L=["Network" , "Math" , "Programming", "Physics" , "Music"]
l=[]
for i in L:
    if i[0] == 'P':
        l.append(i)
x=len(l)
print("there is "+str(x)+" word start with p"+str(l))