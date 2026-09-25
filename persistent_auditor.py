inventory = 0
failed_attempts = 0
processed_delivery = 0

def load_orders(filename="inventory.txt"):
    orders = []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return orders

    for line in lines:
        line = line.strip()
        if not line:
            continue
        order_id, name, qty = line.split(",")
        orders.append((int(order_id), name, int(qty)))
    return orders

def save_order(order, filename="inventory.txt"):
    with open(filename, "a") as f:  # append, since each order saves immediately
        f.write(f"{order[0]},{order[1]},{order[2]}\n")

def generate_next_id(orders):
    if not orders:
        return 1001
    return orders[-1][0] + 1

def get_order_details():
    name = input("\nEnter Product Name: ")
    if name.lower() == 'quit':
        return 'quit'
    qty = input("Enter Quantity: ")
    if not qty.isdigit():
        print("Please enter a valid quantity")
        return None
    return name, int(qty)

def display_orders(orders):
    print("Current Orders:")
    for order in orders:
        print(f"{order[0]}, {order[1]}, {order[2]}")
    print()

def process_delivery(current_total, newStock):
    new_total = current_total + newStock
    return int(new_total)

def calculate_tax(newStock):
    tax = newStock * 0.1
    return tax

def generate_report(deliveryProcessed, failedAttempts, totalInventory):
    print(f"Total Delivery Processed: {deliveryProcessed}")
    print(f"Total Failed Attempts: {failedAttempts}")
    print(f"Total Inventory Received: {totalInventory}")

orders = load_orders()
display_orders(orders)

while True:
    details = get_order_details()

    if details == 'quit':
        print("GoodBye!")
        break

    if details is None:
        continue

    name, qty = details
    new_id = generate_next_id(orders)
    new_order = (new_id, name, qty)

    orders.append(new_order)
    save_order(new_order)

    print(f"\nNew Order Added:\n{new_order[0]}, {new_order[1]}, {new_order[2]}\n")
    print("Order successfully saved to inventory.txt\n")

    display_orders(orders)