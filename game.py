import random

def main():

    #get user input
    def UserInput():
        #ask user until input is a number
        while True:
            #get user input
            n = input("Level: ")
            #check if user input is a number
            if n.isdigit():
                #convert str to integer
                n = int(n)
                #if it is a positive integer return the value
                if n > 1:
                    return n


    #get random integer
    def randint(n):
        #return the value of the random integer chosen by "random" module
        return random.randint(1,n)

    #compare user guess input to actual random number
    def guess(number):
        while True:
            #take user's guess
            guess = input("Guess: ")
            #check guess for integer
            if guess.isdigit():
                #convert str to int
                guess = int(guess)
                #check if guess is the random number
                if guess == number:
                    #print the result and end the while loop
                    print("Just right!")
                    break
                    #check if number is bigger than random number and print
                    #too large
                elif guess > number:
                    print("Too large!")
                    #check if number is lower than random number and print too small
                elif guess < number:
                    print("Too small!")

    # set return value of UserInput funcition to n
    n = UserInput()
    #set return value of UserInput function to number and provide randint with a variable
    number = randint(n)
    #call "guess" function and give it the variable number
    guess(number)

if __name__ == '__main__':
    main()
