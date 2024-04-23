x=int(input("enter the first number"))
y=int(input("enter the second number"))
symbol=input("enter any of the basic symbol to perform airthmetic operation:+,-,*,/:  ")
if (symbol=="+"):
    z=x+y
elif(symbol=="-"):
    z=x-y
elif(symbol=="*"):
    z=x*y
elif(symbol=="/"):
    z=x/y
print(z)