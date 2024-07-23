products = []

while True:
    product_name = input("Enter a product name (or type 'exit' to finish): ")

    if product_name.lower() == 'exit':
        break

    products.append(product_name)

unique_products = []

for product in products:
    if product not in unique_products:
        unique_products.append(product)

print("\nProduct Counts:")
for product in unique_products:
    count = products.count(product)
    print(product + ": " + '*' * count)
