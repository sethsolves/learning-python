from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

# Inventory list to store products
inventory = {}


def update_inventory():
    product_name = product.get()
    price_value = price.get()
    count_value = count.get()
    person_value = person.get()

    if not product_name or not price_value or not count_value or not person_value:
        msg.showerror(title="Error", message="Please fill all the fields")
        return

    try:
        count_value = int(count_value)
        price_value = float(price_value)
    except ValueError:
        msg.showerror(title="Error", message="Price must be a number and Count must be an integer")
        return

    if product_name not in inventory:
        inventory[product_name] = {"price": price_value, "count": 0}

    if in_button.get():
        inventory[product_name]["count"] += count_value
    elif out_button.get():
        if inventory[product_name]["count"] < count_value:
            msg.showerror(title="Error", message="Not enough items in inventory")
            return
        inventory[product_name]["count"] -= count_value
    else:
        msg.showerror(title="Error", message="Please select 'In' or 'Out'")
        return

    msg.showinfo(title="Inventory Update", message=f"Product '{product_name}' updated successfully")
    refresh_table()

    # Clear inputs
    product.set("")
    price.set("")
    count.set("")
    person.set("")
    in_button.set(False)
    out_button.set(False)


def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for product_name, details in inventory.items():
        table.insert(parent="", index=END, values=(product_name, details["price"], details["count"]))


# GUI Setup
win = Tk()
win.geometry("850x350")
win.title("Inventory")

product = StringVar()
price = StringVar()
count = StringVar()
person = StringVar()
in_button = BooleanVar()
out_button = BooleanVar()

Label(win, text="Product").place(x=20, y=20)
Entry(win, textvariable=product).place(x=100, y=20)

Label(win, text="Price").place(x=20, y=60)
Entry(win, textvariable=price).place(x=100, y=60)

Label(win, text="Count").place(x=20, y=100)
Entry(win, textvariable=count).place(x=100, y=100)

Label(win, text="Person").place(x=20, y=140)
Entry(win, textvariable=person).place(x=100, y=140)

Checkbutton(win, text="In", variable=in_button).place(x=20, y=180)
Checkbutton(win, text="Out", variable=out_button).place(x=80, y=180)

Button(win, text="Update", width=10, command=update_inventory).place(x=20, y=220)

table = ttk.Treeview(win, columns=(1, 2, 3), height=12, show="headings")
table.heading(1, text="Product")
table.heading(2, text="Price")
table.heading(3, text="Count")

table.column(1, width=200)
table.column(2, width=150)
table.column(3, width=150)

table.place(x=300, y=20)

refresh_table()

win.mainloop()
