inventory = 0
failed_attempts = 0
processed_delivery = 0

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
    return new_total

def calculate_tax(newStock):
    tax = newStock * 0.1
    return tax

def generate_report(deliveryProcessed, failedAttempts):
    print(f"Total Delivery Processed: {deliveryProcessed}")
    print(f"Total Failed Attemps: {failedAttempts}")

while True:
    stock = get_valid_input()
    if stock == 'quit':
        generate_report(inventory, failed_attempts)
        print("GoodBye!")
    if stock is None:
        failed_attempts += 1
        continue
    inventory = process_delivery(inventory, stock)
    tax = calculate_tax
    print(f"Tax for this delivery: {tax}")
    processed_delivery += 1

