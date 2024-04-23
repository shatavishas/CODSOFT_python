import random
while i<=8:
    x=''.join(chr(random.randint(33,126)))
    i+=1
print("your new password is:")
print(x)
