def main():
    plate = input("Plate: ")
    print(is_valid(plate))



def is_valid(s):

    plate = list(s)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    forbidden_signs = ". !?_-,"
    numbers = "1234567890"
    check_number = []

    #str must start with 2 letters
    def letter(s):
        if s[0] not in letters or s[1] not in letters :
            return False
        return True


    #str can have a maximum of 6 characters an atleast 2
    def char(s):
        if len(s) > 6 or len(s) < 2:
            return False
        return True


    #return false if number is in the middle and or 0 is first number
    def number(s):
        first_number = False
        for char in range(2, len(s)):
            if s[char] in numbers:
                if s[char] == "0" and not first_number:
                    return False
                first_number = True
            elif first_number:
                return False
        return True

    #see if there are periods,spaces, or punctuation marks
    def space(s):
        for i in s:
            if i in forbidden_signs:
                return False

        return True


    if char(plate) and letter(plate) and number(plate) and space(plate) == True:
        return True
    else:
        return False




if __name__ == "__main__":
    main()
