import re

print("<National ID Pattern>")
national_id = input("Enter your national ID: ")

if re.match("^[0-9]{10}$", national_id):
    print("OK", national_id)
else:
    print("Invalid national ID")