import re

print("<Phone Number Pattern>")
phone_number = input("Enter your phone number: ")

if re.match(r"(09|\+989)[0-9]{9}", phone_number):
    print("OK", phone_number)
else:
    print("Invalid phone number")
