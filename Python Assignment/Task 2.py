budget = int(input("Enter Your budget : "))
products = {}
while budget > 0:
    print("1.Add an item \n2.Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        product = input("Enter product : ")
        quantity = input("Enter quantity : ")
        price = int(input("Enter Price : "))
        if price < budget:
            products[product] = (quantity, price)
            budget -= price
            print("Amount left :", budget)
        else:
            print(
                f"Can't Buy the product ###(because budget left is {budget})")
    elif choice == 2:
        break
    else:
        print("Enter correct options,Please.")
print("GROCERY LIST is:")
print("{:<15} {:<8} {:<8}".format('Product name', 'Quantity', 'Price'))
for item in products:
    print("{:<15} {:<8} {:<8}".format(
        item, products[item][0], products[item][1]))
