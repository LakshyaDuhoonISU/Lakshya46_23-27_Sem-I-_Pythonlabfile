#WAP to extend a list in python by using given approach
a=[1,2,3,4,5]
c=[]
b=int(input("Enter number of elements: "))
for i in range(b):
    d=int(input("Enter element: "))
    c.append(d)
a+=c #using + operator
print(a)

b=int(input("Enter element: "))
a.append(b) #using append()
print(a)

c=[]
b=int(input("Enter number of elements: "))
for i in range(b):
    d=int(input("Enter element: "))
    c.append(d)
a.extend(c) #using extend()
print(a)