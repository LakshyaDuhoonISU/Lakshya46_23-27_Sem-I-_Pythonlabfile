#WAP to traverse a list in reverse order by using Reverse method
a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    b=int(input("Enter an element: "))
    a.append(b)
print(a)
a.reverse()
print("Reversed list:",a)