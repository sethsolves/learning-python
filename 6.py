name_list = []
higher_list = []
lower_list = []

while (name := str(input('Enter a name to search: ')).lower()) != "exit":
    name_list.append(name)

for name in name_list:
    if len(name) > 5:
        higher_list.append(name)
    else:
        lower_list.append(name)

print(higher_list)
print(lower_list)
