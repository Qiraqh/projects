import sys


def main():
    read_file()


def read_file():
    lines_in_file = 0
    try:
        path = sys.argv[1]
        if not path.endswith('.py'):
             sys.exit("Not a Python file")
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.lstrip().startswith('#'):
                    pass
                elif line.lstrip() =='':
                    pass
                else:
                    lines_in_file += 1
        print(lines_in_file)

    #checking errors
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
