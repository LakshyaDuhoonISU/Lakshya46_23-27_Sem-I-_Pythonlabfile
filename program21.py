#wap that defines a list of countries that are a member of BRICS and check whether a country is a member of BRICS or not.
brics=["brazil","russia","india","china","south africa"]
a=input("Enter a country: ")
if a.lower() in brics:
    print(a,"is a member of BRICS")
else:
    print(a,"is not a member of BRICS")