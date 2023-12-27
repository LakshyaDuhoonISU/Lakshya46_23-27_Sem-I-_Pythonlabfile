#WAP to Create Employee Class & add methods to get employee details & print.
class Employee:
    __name=""
    __age=0
    __salary=0
    _post=""
    def setData(self):
        name=input("Enter employee name: ")
        self.__name=name
        age=int(input("Enter age of employee: "))
        self.__age=age
        salary=float(input("Enter salary of employee: "))
        self.__salary=salary
        post=input("Enter post of employee: ")
        self.__post=post
    def getData(self):
        print("\nEmployee Data:")
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Salary:", self.__salary)
        print("Post:", self.__post)
a=Employee()
a.setData()
a.getData()