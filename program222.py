#WAP to traverse a list in reverse order by slicing
a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    b=int(input("Enter an element: "))
    a.append(b)
print(a)
print("Reversed list:",a[::-1])