x = int(input("Enter a number: "))

abs_x = abs(x)

print("printing the range from", -abs_x, "to", abs_x)
for i in range(-abs_x, abs_x + 1):
    print(i)
