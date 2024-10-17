def main():
    #get user input as an int
    user = input("What time is it? ")


    #determine if it is a meal time or not
    time = convert(user)
    if time >= 7 and time <=8 :
        print("breakfast time")
    elif time >= 12 and time <=13 :
        print("lunch time")
    elif time >= 18 and time <=19:
        print("dinner time")


def convert(time):
    #split the input and only display the first number
    a,b = time.split(":")
    number1 = int(a)
    number2 = int(b)
    b_in_decimal = number2 / 60

    result = number1+b_in_decimal
    return result

if __name__ == "__main__":
    main()
