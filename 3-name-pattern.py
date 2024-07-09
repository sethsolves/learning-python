import re

print("<Name Pattern>")
name = input("Enter your name: ")

if re.match("^[a-zA-Z\s]+$", name):
    print("OK", name)
else:
    print("Invalid name.")
