def convert(str):
    #replace emoticons with emojis
    new_string=str.replace(':)','🙂').replace(':(','🙁' )
    #returns the string with emoticons converted to emojis
    return new_string


def main():
    #get user's input
    str = input('Please input text ')
    #run it through the convert functions
    new_string=convert(str)
    #prints text
    print(new_string)

main()
