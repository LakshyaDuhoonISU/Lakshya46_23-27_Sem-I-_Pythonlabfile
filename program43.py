#WAP to admit the students in the different Departments(pgdm/btech)and count the students. (Class, Object and Constructor).
class ITM:
    count=0
    bcount=0
    pcount=0
    def __init__(self):
        self.count=0
        self.bcount=0
        self.pcount=0
    def getData(self):
        a=input("Enter student name:" )
        b=int(input("Enter age: "))
        c=input("Enter address: ")
        d=int(input("Select department(1/2):\n1.BTECH\n2.PGDM\n"))
        while not(d==1 or d==2):
            print("Invalid choice\n")
            d=int(input("Select department(1/2):\n1.BTECH\n2.PGDM\n"))
        if d==1:
            self.dep="BTECH"
            ITM.bcount+=1
        elif d==2:
            self.dep="PGDM"
            ITM.pcount+=1
        self.name=a
        self.age=b
        self.address=c
        ITM.count+=1
    def setData(self):
        print("Student Details:\n")
        print("Name:",self.name)
        print("\nAge:",self.age)
        print("\nAddress:",self.address)
        print("\nDepartment:",self.dep)
a=int(input("Welcome to ITM. Press:\n1.Enter Student Data\n2.Number of admissions\n3.Display students data\n4.Exit\n"))
objs=list()
while a!=4:
    if a==1:
        d=int(input("Enter number of students: "))
        for i in range(d):
            objs.append(ITM())
        for i in range(d):
            objs[i].getData()
        a=int(input("\nPress\n1.Enter another data\n2.Number of admissions\n3.Display student details\n4.Exit\n"))
    elif a==2:
        b=int(input("Press\n1.BTECH admissions\n2.PGDM admissions\n"))
        while not (b==1 or b==2):
            print("Invalid choice\n")
            b=int(input("Press\n1.BTECH admissions\n2.PGDM admissions\n"))
        if b==1:
            print("Admissions of BTECH Done:",ITM.bcount)
            print("Total admissions:",ITM.count)
            a=int(input("\nPress\n1.Enter student data\n2.Number of admissions\n3.Display student details\n4.Exit\n"))
        elif b==2:
            print("Admissions of PGDM Done:",ITM.pcount)
            print("Total admissions:",ITM.count)
            a=int(input("\nPress\n1.Enter student data\n2.Number of admissions\n3.Display student details\n4.Exit\n"))
    elif a==3:
        b=int(input("\nPress\n1.For BTECH students data\n2.For PGDM students data\n"))
        if b==1:
            for i in range(d):
                if objs[i].dep=="BTECH":
                    objs[i].setData()
            a=int(input("\nPress\n1.Enter student data\n2.Number of admissions\n3.Display student details\n4.Exit\n"))
        elif b==2:
            for i in range(d):
                if objs[i].dep=="PGDM":
                    objs[i].setData()
            a=int(input("\nPress\n1.Enter student data\n2.Number of admissions\n3.Display student details\n4.Exit\n"))
        else:
            print("Invalid choice")
            a=int(input("\nPress\n1.Enter student data\n2.Number of admissions\n3.Display student details\n4.Exit\n"))
    elif a==4:
        break
    else:
        print("Invalid choice")
        break