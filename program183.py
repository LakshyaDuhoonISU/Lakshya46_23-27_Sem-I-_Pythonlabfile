#WAP to ascending pyramid pattern
for i in range(1,6):
    for j in range(6,i,-1): #pyramid pattern ascending
        print(" ",end='')
    for k in range(2*i-1):
        print("*",end='')
    print()