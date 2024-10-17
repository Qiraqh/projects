def main():
    #take user's input of mass and converting to an integer
    m=int(input("Please choose a number "))

    def mass():

        # defining the speed of light
        c= 300000000

        #defining the mathematical function of E
        E=m*(c*c)

        #returning the value of the function
        return E
    #calling function 'mass()'
    mass()
    solution=mass()
    #print the variable solution
    print(solution)

#calling the function 'main()'
main()

