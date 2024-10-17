import sys
import csv


def main():




    try:
        csv_to_read = sys.argv[1]
        csv_to_write = sys.argv[2]
        if not csv_to_read.endswith('.csv') or not csv_to_write.endswith('.csv'):
             sys.exit("Not a CSV file")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        #read the first file
        students = []
        with open(csv_to_read) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name":row["name"], "house": row["house"]})

        order = []
        for student in students:
            full_name = student['name']
            house = student['house']
            last, first = full_name.strip('"').split(",")
            first = first.strip()
            last = last.strip()
            order.append({'first': first,'last':last,'house':house})


        fieldnames = ['first', 'last', 'house']

        with open(csv_to_write, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in order:
                writer.writerow(student)

    except FileNotFoundError:
      sys.exit(f"Could not read {csv_to_read}")

    except IndexError:
        sys.exit("Too few command-line arguments")

if __name__=='__main__':
    main()
