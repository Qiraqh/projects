def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #get rid of dollar sign
    dollar_amount=d.strip("$")
    #format str into float
    decimal= float(dollar_amount)
    #get only 2 decimal places and retrun value
    return(round(decimal,2))


def percent_to_float(p):
    #get rid of the %
    percent_amount=p.strip("%")
    #format str into float and divide by 100 to get % into decimal
    decimal=float(percent_amount)/100
    #return value with 2 decimals
    return(round(decimal,2))


main()
