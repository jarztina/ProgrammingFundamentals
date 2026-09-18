inventory = 0
failed_attempts = 0

def get_valid_input():
    stock = input("Enter the stock quantity: ")
    if stock == 'quit':
        return 'quit' 
    if not stock.isdigit():
        print("Please enter a valid stock quantity")
        return None
    else:
        return stock


while True:
    stock = get_valid_input()
    if stock == 'quit':
        print("GoodBye!")
    if stock is None:
        failed_attempts += 1
        continue
    process_delivery(inventory, stock)
    