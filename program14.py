#WAP to print first n Natural numbers and their sum.
a=int(input("Enter a number: "))
sum=0
if a<=0:
    print("Invalid number!")
else:
    for i in range(1,a+1):
        print(i)
        sum+=i
    print("Sum:",sum)