def main():

    #get user input
    user = input("Expression: ")
    x,y,z = user.split()

    number_x = float(x)

    number_z = float(z)


    if y == '+':
        print(f"{number_x + number_z:.1f}")

    elif y == '-':
        print(f"{number_x - number_z:.1f}")

    elif y == '*':
        print(f"{number_x * number_z:.1f}")

    elif y == '/':
        print(f"{number_x / number_z:.1f}")



main()
