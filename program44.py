#WAP that has a class store which keeps the record of code and price of product display the menu of all product and prompt to enter the quantity of each item required and finally generate the bill and display the total amount.
class Store:
    __itemCode=0
    __price=0
    __total=0
    product=[]
    quantity=[]
    price=[]
    def __init__(self):
        print("Welcome to ABC Store!")
        while True:
            a=int(input("Select a product:\n1.Soap\n2.Toothbrush\n3.Toothpaste\n4.Comb\n5.Book\n"))
            c=("Soap","Toothbrush","Toothpaste","Comb","Book")
            if a==1:
                self.__itemCode=1
                self.__price=50
            elif a==2:
                self.__itemCode=2
                self.__price=100
            elif a==3:
                self.__itemCode=3
                self.__price=200
            elif a==4:
                self.__itemCode=4
                self.__price=150
            elif a==5:
                self.__itemCode=5
                self.__price=500
            print("Product:",c[a-1],"\nPrice:",self.__price)
            self.product.append(c[a-1])
            self.price.append(self.__price)
            b=int(input("Enter the quantity: "))
            while b<=0:
                print("Invalid quantity")
                b=int(input("Enter the quantity: "))
            self.quantity.append(b)
            self.__total+=self.__price*b
            print("Total:",self.__total)
            d=input("Do you want to add more items?(y/n): ")
            if d.lower()=="n":
                break
        print("\t\tBill\n\nProduct\t\tPrice\t\tQuantity")
        for i in range(len(self.product)):
            print(self.product[i],"\t\t",self.price[i],"\t\t",self.quantity[i],"")
        print("Total:",self.__total)
obj=Store()