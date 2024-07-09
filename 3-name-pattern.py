import re

print("<Name Pattern>")
name = input("Enter your name: ")

if re.match(r"([^_.,0-9@$!\-+#*]+)[a-zA-Z\s]{2,}", name):
    print("OK", name)
else:
    print("Invalid name.")
