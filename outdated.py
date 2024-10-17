def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    def get_date():
        while True:

            try:
                date= input("Date: ").title()
                if "/" in date:
                    date = date.replace(",","")
                    a,b,c = date.split("/")
                    a = int(a)
                    b = int(b)
                    c = int(c)

                    if a in range(1,13) and b in range(1,32):

                        print(f'{c}-{a:02}-{b:02}')
                        break



                elif "," in date:
                    date = date.replace(",","")
                    a,b,c = date.split(" ")
                    if int(b) in range(1,32):
                        b = int(b)
                        c = int(c)
                        m_to_d = months.index(a)
                        a = int(m_to_d) + 1
                        print(f'{c}-{a:02}-{b:02}')
                        break
            except ValueError:
                print()

    get_date()







main()

