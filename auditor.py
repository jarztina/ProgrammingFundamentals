quantity = 0
count = 0
stock = 0
choice = 0

while choice != 2:
    if quantity <= 500:
        #Menu page
        print("\n==== Auditor Program ====")
        print(f"Stock Quantity: {quantity}")
        print("1. Update Stock")
        print("2. Quit")

        while True:
            choice = input("Enter Choice: ")
            if choice.isdigit():
                break;
            print("\nInvalid Choice Selection!")

        #will only get here if user inputs correct choice selection
        choice = int(choice)

        if choice == 1:
            #user input amount of stock to add:
            while True:
                stock = input("Enter Stock Quantity: ")

            #check whether stock input is int:
                if not stock.isdigit():
                    print("\nInvalid Stock Amount")
                    count += 1
                    continue
            #delcare stock is integer
                stock = int(stock)
            #will only run if stock is a digit
                if stock <= 0:
                    print("\nInvalid Stock Amount")
                    count += 1
                    continue

                break #only breaks when valid int and positive

            quantity += stock

        elif choice == 2:
            print(f"Total Unit Processed: {quantity}")
            print(f"Failed/Rejected Entries: {count}")
            print("\nGoodBye!")

        else:
            continue
    else:
        print("\nOverstocked! Exiting...")
        break