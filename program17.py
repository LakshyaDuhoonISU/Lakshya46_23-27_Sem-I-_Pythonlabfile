#WAP to calculate factorial of a number using for loop
a=int(input("Enter a number: "))
fact=1
if a<0:
    print("Invalid number")
elif a==0 or a==1:
    print("Factorial:",1)
else:
    for i in range(1,a+1):
        fact*=i
    print("Factorial:",fact)