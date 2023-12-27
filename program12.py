#WAP to perform arithmetic and relational calculation.
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=input("Select the operator: +,-,/,*,%,//,** ")
if c=="+":
    print("Sum:",a+b)
elif c=="-":
    print("Difference:",a-b)
elif c=="*":
    print("Multiplication:",a*b)
elif c=="/":
    print("Division:",a/b)
elif c=="%":
    print("Remainder:",a%b)
elif c=="//":
    print("Floor division:",a//b)
elif c=="**":
    print("Power:",a**b)
else:
    print("Invalid operator!")
if a>b:
    print(a,"is greater than",b)
elif a==b:
    print(a,"is equal to",b)
else:
    print(b,"is greater than",a)