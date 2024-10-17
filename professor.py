import random

def main():
    level = get_level()
    problems_solved = 0
    correct_answers = 0

    while problems_solved < 10:
        times_tried = 0
        randint1 = generate_integer(level)
        randint2 = generate_integer(level)
        sum_of_numbers = randint1 + randint2

        while True:

            answer = int(input(f'{randint1} + {randint2} = '))
            if answer == sum_of_numbers:
                break
            if answer != sum_of_numbers:
                print('EEE')
                times_tried +=1

            if times_tried == 3:
                print(f'{randint1} + {randint2} = {sum_of_numbers}')
                break
        if answer == sum_of_numbers:
            correct_answers += 1

        problems_solved += 1

    print(f'score: {correct_answers}')



def get_level():
    while True:
        n = input("Level: ")
        if n.isdigit():
            n = int(n)
            if n in range(1,4):
                return n



def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError







if __name__ == "__main__":
    main()
