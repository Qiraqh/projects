def main():
    user = value(input("Greeting: "))
    print(user)

    if user.startswith("hello"):
        print("$0")

    elif user.startswith("h"):
        print("$20")

    else:
        print("$100")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0

    elif greeting.startswith("h"):
        return 20

    else:
        return 100



if __name__ == "__main__":
    main()

