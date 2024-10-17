class Jar:
    #set capacity of cookies to 12 which should be the maximum amount
    #if capacity is not 0 or higher int raise ValueError
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.cookies_left = 0

    #return cookie emojis for how many cookies there are left in the jar
    def __str__(self):
        return"🍪" * self.cookies_left


    #add cookies to the jar until full and if full then raise ValueError
    def deposit(self, n):
        if self.cookies_left + n > self._capacity:
            raise ValueError("Cannot deposit more cookies than the jar can hold")
        self.cookies_left += n

    #remove amount of cookies from jar if there arent enough left raise ValueError
    def withdraw(self, n):
        if self.cookies_left - n < 0:
            raise ValueError("There arent any more cookies inside the jar")
        self.cookies_left -= n



    #return the cookie jars capacity
    @property #getter
    def capacity(self):
        return self._capacity


    #return number of cookies
    @property
    def size(self):
        return self.cookies_left

