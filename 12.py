from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

product_list = []


def save_click():
    # Validation
    option = "glass" if glass.get() else "memory" if memory.get() else "none"
    product = (brand.get(), model.get(), color.get(), option)

    print(product)
    product_list.append(product)

    msg.showinfo(title="Product Save", message="Product " + str(product) + " saved")
    refresh_table()

    brand.set("")
    model.set("")
    color.set("")
    glass.set(False)
    memory.set(False)


def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for product in product_list:
        table.insert(parent="", index=END, values=product, tags=product[3])


win = Tk()

win.geometry("650x300")
win.title("Product")

brand = StringVar()
model = StringVar()
color = StringVar()
glass = BooleanVar()
memory = BooleanVar()

brand_combo = ttk.Combobox(win, state="readonly", textvariable=brand, values=["apple", "samsung", "nokia"])
brand_combo.place(x=80, y=20)
brand_combo.current(0)

Label(win, text="brand").place(x=20, y=20)
Label(win, text="model").place(x=20, y=60)
Label(win, text="color").place(x=20, y=100)
Label(win, text="option").place(x=20, y=140)

Entry(win, textvariable=model).place(x=80, y=60)

color_combo = ttk.Combobox(win, state="readonly", textvariable=color, values=["white", "black", "red", "blue"])
color_combo.place(x=80, y=100)
color_combo.current(0)

Checkbutton(win, text="glass", variable=glass).place(x=80, y=140)
Checkbutton(win, text="memory", variable=memory).place(x=80, y=180)

Button(win, text="Sell", width=10, command=save_click).place(x=20, y=240)

table = ttk.Treeview(win, columns=(1, 2, 3, 4), height=12, show="headings")
table.heading(1, text="brand")
table.heading(2, text="model")
table.heading(3, text="color")
table.heading(4, text="option")

table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)

table.place(x=230, y=20)

refresh_table()

win.mainloop()
