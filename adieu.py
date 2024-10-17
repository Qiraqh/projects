import inflect
p = inflect.engine()


def main():

    #store the names
    names = []

    #get names until ctrl+d is used
    while True:

        try:
            #get user input
            name = input("Name: ")
            #store name in 'names' list
            names.append(name)
        #when control+d is used
        except EOFError:
            #join the words in list to a new list with last sep= and
            names = p.join(names)
            #print result
            print(f'Adieu, adieu, to {names}')
            #end program
            break



if __name__ == '__main__':
    main()
