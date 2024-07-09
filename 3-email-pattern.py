import re

print("<Email Address Pattern>")
email = input("Enter your email: ")

if re.match(r"([^,_.0-9]+)[a-zA-Z0-9_.]{6,30}@(gmail|yahoo|msn)\.com", email):
    print("OK", email)
else:
    print("Invalid email address.")
