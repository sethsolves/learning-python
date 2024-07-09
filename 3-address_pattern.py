import re

print("<Address Pattern>")
address = input("Enter your Address: ")

if re.match("^[0-9a-zA-z\s\-]+$", address):
    print("OK", address)
else:
    print("Invalid address.")
