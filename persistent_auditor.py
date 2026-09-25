inventory = 0
failed_attempts = 0
processed_delivery = 0

def load_inventory(filename = "inventory.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines():
    except FileNotFoundError:
        return 0, []

    if not lines:
        return 0, []

    total = int(lines[0].strip())
    history = [int(line.strip()) for line in lines[1:] if line.strip()]
    return total, history

def save_inventory(inventory, history, filename = "inventory.txt"):
    with open(filename = "w") as f:
        f.write(f"{inventory}\n")
        for amount in history:
            f.write(f"{amount}\n")

def get_valid_input():
    stock = input("Enter the stock quantity: ")
    if stock == 'quit':
        return 'quit' 
    if not stock.isdigit():
        print("Please enter a valid stock quantity")
        return None
    else:
        return int(stock)

def process_delivery(current_total, newStock):
    new_total = current_total + newStock
    return int(new_total)

def calculate_tax(newStock):
    tax = newStock * 0.1
    return tax

def generate_report(deliveryProcessed, failedAttempts, totalInventory):
    print(f"Total Delivery Processed: {deliveryProcessed}")
    print(f"Total Failed Attempts: {failedAttempts}")
    print(f"Total Inventory Receivedz: {totalInventory}")

inventory, history = load_inventory()

while True:
    stock = get_valid_input()

    if stock == 'quit':
        generate_report(processed_delivery, failed_attempts, inventory)
        print("GoodBye!")
        break

    if stock is None:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, stock)
    tax = calculate_tax(stock)
    print(f"Tax for this delivery: {tax}")
    processed_delivery += 1


