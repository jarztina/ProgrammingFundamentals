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
