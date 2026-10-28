import json
from product import Product
from inventory import Inventory

def load_inventory(filename="inventory.json"):
    inventory = Inventory()
    try:
        with open(filename, "r") as f:
            for d in json.load(f):
                inventory.add_product(
                    Product(d["id"], d["name"], d["price"], d["stock"]))
            print("Inventory Loaded Successfully")
    except FileNotFoundError:
        pass
    return inventory

def save_inventory(inventory, filename = "inventory.json"):
    with open(filename, "w") as f:
        json.dump(inventory.to_list(), f, indent=4)
    print("Inventory Saved Successfully")


def get_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    get_choice = input("Enter Choice: ")
    if not get_choice.isdigit():
        print("Enter Valid Choice!")
        return None
    return int(get_choice)

inventory = load_inventory()

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")
while True:
    choice = get_menu()
    if choice is None:
        continue
    elif choice == 1:
        inventory.display_all()
    elif choice == 2:
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        try:
            price = float(input("Enter Product Price: "))
            stock = int(input("Stock Quantity: "))
        except ValueError:
            print("Invalid price or stock!")
            continue
        if inventory.add_product(Product(product_id, name, price, stock)):
            print("Product Added Successfully!")
        else:
            print("Product ID already exists!")
    elif choice == 3:
        product = inventory.search_product(input("Enter Product ID: "))
        if product is None:
            print("Product Not Found!")
        else:
            try:
                new_stock = int(input("New Stock Quantity: "))
            except ValueError:
                print("Invalid number!")
                continue
            if product.update_stock(new_stock):
                print("Stock Updated Successfully")
            else:
                print("Stock cannot be negative!")
    elif choice == 4:
        product = inventory.search_product(input("Enter Product ID: "))
        if product is None:
            print("Product Not Found")
        else:
            product.display_information()
    elif choice == 5:
        save_inventory(inventory)
    elif choice == 6:
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated")
        break