from random import choice
from pyfiglet import Figlet
import sys
figlet = Figlet()


def main():

    #get all fonts into a list
    fonts = figlet.getFonts()
    #checks length ob command line arguments and if there is something wrong exits
    if len(sys.argv) >= 2:
        if sys.argv[1] != '-f' and sys.argv[1] != '--font':
            sys.exit('Invalid usage')
        elif sys.argv[2] not in fonts:
            sys.exit('Invalid usage')

    #get user input
    str = input('Input: ')


    #outputs a random font if user wants so
    if len(sys.argv) < 2:

        #picks a random font
        r= choice(fonts)
        #sets the font
        figlet.setFont(r)
        #print formattet text
        print(figlet.renderText(str))


    #looks if user wants a font
    elif sys.argv[1] == '-f' or sys.argv[1] == '--font':

        #see which font user has chosen
        user_font = sys.argv[2]

        #set font to what the user wants
        figlet.setFont(font = user_font)

        #print formattet text
        print(figlet.renderText(str))





if __name__ == '__main__':

    main()
