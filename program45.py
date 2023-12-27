#WAP to take input from user for addition of two numbers using (single inheritance).
class Addition:
    def add(a,b):
        print("Sum:",a+b)
class Numbers(Addition):
    def getNumbers(self):
        c=float(input("Enter a number: "))
        d=float(input("Enter another number: "))
        Addition.add(c,d)
e=Numbers()
e.getNumbers()