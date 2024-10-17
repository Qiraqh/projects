def main():

    #amount which has to be paid
    amount_due = 50

    #if amount is paid amount due shall not be displayed
    if amount_due > 0:
        print("Amount Due:", amount_due)

    #get the insert amount in cents
    amount_in_cents = int(input("Insert Coin: "))

    #price of one coke bottle
    coke_price = 50
    #money which was already put in
    money_in = 0



    while money_in < coke_price:
        if amount_in_cents in [25, 10, 5]:
            money_in += amount_in_cents
            amount_due -= amount_in_cents
            if amount_due > 0:
                print("Amount Due:",amount_due)
                amount_in_cents = int(input("Insert Coin: "))

        else:
            print("Amount Due:", amount_due)
            amount_in_cents = int(input("Insert Coin: "))


    #how much change is owed
    change_owed = money_in - coke_price
    print("Change Owed:",change_owed)


main()
