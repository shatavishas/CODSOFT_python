x=int(input("enter the first number"))
y=int(input("enter the second number"))
symbol=input("enter any of the basic symbol to perform airthmetic operation:+,-,*,/:  ")
if (symbol=="+"):
    z=x+y
    print("the sum of the two numbers is:")
elif(symbol=="-"):
    z=x-y
    print("the difference of the two numbers is:")
elif(symbol=="*"):
    z=x*y
    print("the product of the two numbers is:")
elif(symbol=="/"):
    z=x/y
    print("the division of the two numbers gives:")
print(z)
