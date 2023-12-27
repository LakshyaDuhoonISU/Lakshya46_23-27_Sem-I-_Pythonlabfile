#WAP Design the Library catalogue system using inheritance take base class (library item) and derived class (Book, DVD & Journal) Each derived class should have unique attribute and methods and system should support Check in and check out the system. (Using Inheritance and Method overriding)
class Library_item:
        _bookCount=0
        _dvdCount=0
        _journalCount=0
        quantity=[]
        cart=[]
class Book(Library_item):
    def __init__(self):
        super().__init__()
        def check_out_book(self):
            d=int(input("How many books you want to select?: "))
            if d>4:
                print("Invalid choice")
            else:
                for i in range(d):
                    c=int(input("Select a book: "))
                    f=int(input("Enter quantity: "))
                    Library_item.quantity.append(f)
                    self.cart.append(a[c-1])
                    Library_item._bookCount+=1
                print(self.cart)
                print("Books selected:",Library_item._bookCount)
        a=["C programming by Ritchie-Cunningham","C++ by Balaguruswamy","R.D. Sharma","Class 12 CS by NCERT"]
        b=1
        for i in range(len(a)):
            print(b,a[i])
            b+=1
        check_out_book(self)
class Dvd(Library_item):
    def __init__(self):
        super().__init__()
        def check_out_dvd(self):
            d=int(input("How many DVD's you want to select?: "))
            for i in range(d):
                if d>4:
                    print("Invalid choice")
                else:
                    c=int(input("Select a DVD: "))
                    f=int(input("Enter quantity: "))
                    Library_item.quantity.append(f)
                    self.cart.append(a[c-1])
                    Library_item._dvdCount+=1
            print(self.cart)
            print("DVDs selected:",Library_item._dvdCount)
        a=["Avengers","Justice League","Conjuring","ABC"]
        b=1
        for i in range(len(a)):
            print(b,a[i])
            b+=1
        check_out_dvd(self)
class Journal(Library_item):
    def __init__(self):
        super().__init__()
        def check_out_journal(self):
            d=int(input("How many Journal you want to select?: "))
            if d>4:
                print("Invalid choice")
            else:
                for i in range(d):
                    c=int(input("Select a journal: "))
                    f=int(input("Enter quantity: "))
                    Library_item.quantity.append(f)
                    self.cart.append(a[c-1])
                    Library_item._journalCount+=1
                print(self.cart)
                print("Journals selected:",Library_item._journalCount)
        a=["A Journal","XYZ Journal","ABC Journal","QWERTY Journal"]
        b=1
        for i in range(len(a)):
            print(b,a[i])
            b+=1
        check_out_journal(self)
class Checkout(Library_item):
    def __init__(self):
        super().__init__()
        print("\nCheckout")
        j=1
        for i in range(len(self.cart)):
            print(j,self.cart[i],"-",self.quantity[i])
            j+=1
        print("\nBooks selected:",self._bookCount)
        print("Journals selected:",self._journalCount)
        print("DVDs selected:",self._dvdCount)
        print("Total:",self._bookCount+self._journalCount+self._dvdCount)
objs=list()
print("Welcome to ABC Library!")
for i in range(100):
    a=int(input("\nPress:\n1.Book Catalogue\n2.DVD Catalogue\n3.Journal Catalogue\n4.Checkout\n5.Exit\n"))
    if a==1:
        objs.append(Book())
    elif a==2:
        objs.append(Dvd())
    elif a==3:
        objs.append(Journal())
    elif a==4:
        objs.append(Checkout())
    elif a==5:
        print("Thank You!")
        break
    else:
        print("Invalid choice")
        break