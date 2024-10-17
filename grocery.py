def main():
    #empty list
    list = []

    #permanent loop
    while True:
        try:

            #get user input in all uppercase
            item = input().upper()

            #put item into the list
            list.append(item)
            list.sort()




        #when pressed ctrl + d
        except EOFError:

            #for the used items
            is_used = []

            #goes over every item in list
            for item in list:

                #count how many items there are and inside of the list of
                #the specific item
                item_quantity = list.count(item)

                if item not in is_used:
                    #print the item quantity aswell as the item and a new line
                    print(f"{item_quantity} {item}")

                    #puts used items into the used list
                    is_used.append(item)
            #ends the loop
            break




main()
