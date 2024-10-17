def main():
    #get user input
    w = shorten(input("Input: "))
    print(w)








def shorten(word):
    #define vowels
    vowels = "AEIOUaeiou"
    #get a new list
    new_list = []
    user_list = list(word)
    #remove vowels from input
    for letter in user_list:
        if letter not in vowels:
            new_list.append(letter)

    return ''.join(new_list)



if __name__ == "__main__":
    main()
