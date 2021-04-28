def caclcpriceofpizza():
    n=int(input("Enter the  number of pizzas you want to buy\n"))
    if n%2==0:
        price=120*n
        print("You have been charged 120 for each pizza ")
    else:
        price=123*n
        print("You have been charged 123 for each pizza ")
    print("The total amount you have to pay is ",price)
    print("Enjoy ! Have a nice day.")