inventory = 0
failed_attempts = 0
processed_delivery = 0

def load_inventory(filename = "inventory.txt"): #defines the function with the parameter of filename
    try: 
        with open(filename, "r") as f: #opens the file in read mode
            lines = f.readlines() #reads the file and returns it as a list of strings
    except FileNotFoundError: #this is used on the first try, with no inventory.txt created
        return 0, [] #starts with empty total and an empty list of strings

    if not lines:
        return 0, [] #stars with empty total and an empty list of strings

    total = int(lines[0].strip()) #convert the first element of the list and convert it into integer
    history = [int(line.strip()) for line in lines[1:] if line.strip()] #line.strip removes the /n infront and behind the string
    return total, history

def save_inventory(inventory, history, filename = "inventory.txt"):
    with open(filename, "w") as f:
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
    print(f"Total Inventory Received: {totalInventory}")

inventory, history = load_inventory()

while True:
    stock = get_valid_input()

    if stock == 'quit':
        save_inventory(inventory, history)
        generate_report(processed_delivery, failed_attempts, inventory)
        print("GoodBye!")
        break

    if stock is None:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, stock)
    history.append(stock)
    tax = calculate_tax(stock)
    print(f"Tax for this delivery: {tax}")
    processed_delivery += 1


