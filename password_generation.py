import random
import string
length=int(input("enter the length of the password"))
passwords = []
for i in range(length):
    password = ''. join(random. choice(string. ascii_letters + string. digits + string. punctuation))
    passwords. append(password)

print(*passwords)
