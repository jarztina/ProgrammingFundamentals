inventory = 0
failed_attempts = 0
deliveries_processed = 0

def get_valid_input():
    stock = input("Enter Stock Quantity: ")
    if stock == 'quit':
        return 'quit'
    if not stock.isdigit():
        print("Enter a valid stock quantity or quit")
        return None
    else:
        return int(stock)
        
def process_delivery(inventory, validStock):
    new_total = inventory + validStock
    return new_total

def calculate_tax(inventory):
    taxAmount = validStock * 0.1
    return taxAmount

def generateReport(inventory, tax):
    totalAmount = inventory + tax
    return totalAmount

while True:
    validStock = get_valid_input() #if valid stock number is entered, it will be stored here

    if validStock == 'quit':
        print("GoodBye!")
        break

    if validStock is None:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, validStock)
    tax = calculate_tax(inventory)
    total = generateReport(inventory, tax)
