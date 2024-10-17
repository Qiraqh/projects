import sys
from datetime import date
import inflect
p = inflect.engine()



def main():

    birth = input("Date of Birth: ")
    print(convert(birth))


def convert(birth):
    try:
        today = date.today()
        b_year, b_month, b_day = birth.split("-")
        b_year, b_month, b_day = int(b_year), int(b_month), int(b_day)
        birthday = Birth(year=b_year, month=b_month, day=b_day)

    except ValueError:
        sys.exit("Invalid Date")
    except TypeError:
        sys.exit("Invalid Date")


    total = today - birthday.date
    minutes = total.days * 24 * 60
    words = p.number_to_words(minutes, andword="").capitalize()
    return(f"{words} minutes")




class Birth:
    def __init__(self, year, month, day):
      try:
        self.date = date(year, month, day)
      except ValueError:
         sys.exit("Invalid Date")

    def __str__(self):
       return self.date.isoformat()

    def __sub__(self, other):
       difference = other - self.date
       #return minutes
       return difference


if __name__ == "__main__":
    main()
