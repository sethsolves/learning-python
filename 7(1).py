cars = []
total_price = 0

while True:
    add_more = input("Do you want to add a car? (yes/no): ").strip().lower()
    if add_more == 'no':
        break

    name = input("Enter car name: ")
    model = input("Enter car model: ")
    price = float(input("Enter car price: "))

    car = (name, model, price)
    cars.append(car)
    total_price += price

print(f"\nTotal number of cars: {len(cars)}")

print("\nCars:")
for car in cars:
    print(f"{car[0]} {car[1]}")

print(f"\nTotal price of all cars: {total_price}")
