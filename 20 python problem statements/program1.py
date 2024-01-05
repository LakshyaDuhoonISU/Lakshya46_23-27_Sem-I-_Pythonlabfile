#WAP to create a person class. Include attributes like name,country and date of birth. Implement a method to determine the person's age.
from datetime import datetime
class Person:
    __name=""
    __country=""
    __day=0
    __month=0
    __year=0
    def __init__(self):
        a=input("Enter your name: ")
        b=input("Enter your country: ")
        c=int(input("Enter your birth date(DD): "))
        d=int(input("Enter your birth month(MM): "))
        e=int(input("Enter your birth year(YYYY): "))
        self.__name=a
        self.__country=b
        self.__day=c
        self.__month=d
        self.__year=e
    def age(self):
        today = datetime.now()
        dob_date = datetime(self.__year, self.__month, self.__day)
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        print("Name:", self.__name)
        print("Country:", self.__country)
        print("Age:", age)
def main():
    a=Person()
    a.age()
if __name__=="__main__":
    main()