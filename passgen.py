import random
#name=input("enter your name")
while i<=8:
    x=''.join(chr(random.randint(65,90)))
    i+=1
print("your new password is:")
print(x)