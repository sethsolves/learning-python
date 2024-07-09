import re

print("<Email Address Pattern>")
email = input("Enter your email: ")

if re.match("^[a-zA-Z0-9_. +-]+@[a-zA-Z0-9-]+\. [a-zA-Z0-9-.]+$", email):
    print("OK", email)
else:
    print("Invalid email address.")
