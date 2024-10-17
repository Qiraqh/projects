def main():
    #user input
    user = input("camelCase: ")
    #perform camel case to snake case on input
    snake_case = camel_to_snake(user)
    #print words in snake case format
    print("snake_case: " + snake_case)




def camel_to_snake(user):
    #list with uppercase letter to seperate on
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #alphbet into list
    uppercase = list(alphabet)
    input_as_list = list(user)
    new_list = []

    for letter in input_as_list:
        if letter in uppercase:
            new_list.append("_")
            new_list.append(letter.lower())

        else:
            new_list.append(letter)


    snake_case = "".join(new_list)

    return snake_case







main()
