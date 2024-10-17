from tabulate import tabulate
import sys
import csv

def main():
    list = []
    try:
        path = sys.argv[1]
        if not path.endswith('.csv'):
             sys.exit("Not a CSV file")
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        with open(path) as file:
            reader = csv.reader(file)
            for row in reader:
                list.append(row)


        print(tabulate(list, headers='firstrow', tablefmt="grid"))


    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
