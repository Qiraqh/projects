def main():

    #get user input and convert to a int
    fraction = convert(input("Fraction: "))
    # turn that int into E, F or percentage
    x = gauge(fraction)

    print(f"{x}")

def convert(fraction):

            #get x and y
            x, y = fraction.split("/")
            #raise Errors
            if x.isnumeric() != True:
                  raise ValueError
            elif y.isnumeric() != True:
                  raise ValueError
            elif y == '0':
                  raise ZeroDivisionError
            elif x > y:
                  raise ValueError

            #turn x and y into integers
            x = int(x)
            y = int(y)
            #turn x and y into percent
            percentage = (x/y) * 100
            return round(percentage)



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99 and percentage< 101:
        return "F"
    elif percentage in range(2,99):
        return f"{percentage}%"









if __name__ == "__main__":
    main()
