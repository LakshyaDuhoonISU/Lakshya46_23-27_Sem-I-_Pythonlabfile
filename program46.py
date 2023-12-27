#WAP to create two base classes LU and ITM and one derived class(Multiple inheritance).
#multiple inheritance
class LU:
    subjects=["AI/ML","AR/VR","Cloud Computing","Full Stack Developer"]
    teachers=["Sai Sir","Swapnil Sir","ABC","XYZ"]
    duration=["60 days","30 days","50 days","55 days"]
class ITM:
    subjects=["Hotel management","BTECH CSE","Design","Business"]
    teachers=["abc","Sumit sir","xyz","qwer"]
    duration=["90 days","120 days","60 days","30 days"]
class Btech(LU,ITM):
    print("LetsUpgrade courses are:\n")
    a=LU.subjects
    j=1
    for i in range(len(a)):
        print(j,LU.subjects[i],"by",LU.teachers[i],"for",LU.duration[i])
        j+=1
    c=[]
    d=int(input("How many subjects you want to select: "))
    if d>4:
        print("Invalid number of subjects")
    else:
        for i in range(d):
            e=int(input("Select your interested course: "))
            c.append(e)
    print("\nITM courses are:\n")
    j=1
    b=ITM.subjects
    for i in range(len(b)):
        print(j,ITM.subjects[i],"by",ITM.teachers[i],"for",ITM.duration[i])
        j+=1
    f=[]
    d=int(input("How many subjects you want to select: "))
    if d>4:
        print("Invalid number of subjects")
    else:
        for i in range(d):
            e=int(input("Select your interested course: "))
            f.append(e)
    j=1
    print("\nYour selected courses are:\n")
    for i in c:
        print(j,LU.subjects[i-1],"by",LU.teachers[i-1],"for",LU.duration[i-1])
        j+=1
    for i in f:
        print(j,ITM.subjects[i-1],"by",ITM.teachers[i-1],"for",ITM.duration[i-1])
        j+=1
obj=Btech()