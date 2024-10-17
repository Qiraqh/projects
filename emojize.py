import emoji


def main():



    #get the user input
    user = input('input: ')

    #print str as emoji
    print(emoji.emojize(f'{user}', language='alias'))











if __name__ == '__main__':
    main()

