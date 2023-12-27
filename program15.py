#WAP to check whether a given character is vowel or not
a=["a","e","i","o","u"]
b=input("Enter a character: ")
if b.lower() in a:
    print(b,"is a vowel")
else:
    print(b,"is not a vowel")