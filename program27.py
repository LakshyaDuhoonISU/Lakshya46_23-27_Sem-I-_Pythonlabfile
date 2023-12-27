#WAP for various list slicing operation.
a= [10,20,30,40,50,60,70,80,90,100]
print(a) #Print Complete list

print(a[3]) #Print 4th element of list

print(a[0:4]) #Print list from0th to 4th index.

print(a[-7:4]) #Print list -7th to 3rd element

a.append(110) #Appending an element to list.
print(a)

a.sort() #Sorting the element of list.
print(a)
a.sort(reverse=True) #Sorting the element of list in descending order.
print(a)

a.pop() #Popping an element.
print(a)

b=int(input("Enter element to remove: "))
if b in a:
    a.remove(b) #Removing Specified element.
    print(a)
else:
    print("Invalid element")

b=int(input("Enter element to add: "))
c=int(input("Enter index where to insert: "))
a.insert(c,b) #Entering an element at specified index.
print(a)

b=int(input("Enter element to count: "))
count=0
for i in a:
    if i==b:
        count+=1 #Counting the occurrence of a specified element.
print("Count of element:",count)

c=int(input("Enter number of elements: "))

d=[]
for i in range(c):
    b=int(input("Enter element: "))
    d.append(b) 
a.extend(d) #Extending list.
print(a)

a.reverse() #Reversing the list.
print(a)