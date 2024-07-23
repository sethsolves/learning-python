numbers = []

for num in range(10):
    number = float(input("Enter a number: "))
    numbers.append(number)

average = sum(numbers) / len(numbers)

print("Numbers bigger than the average:", average)
for number in numbers:
    if number > average:
        print(number)
