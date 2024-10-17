def main():
    menu=   {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}
    #sets total to zero
    total = 0
    while True:

        try:


            #get input with first letters as capital
            user = input("Item: ").title()

            #adds the total with the value of the item from the menu
            total= total+ menu.get(user)

            #prints total with 2 decimals
            print(f"${total:.2f}")

        except EOFError:
            print("\n")
            return
        except (TypeError, KeyError):
            True

main()
