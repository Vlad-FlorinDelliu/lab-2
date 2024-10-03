def evenOddChecker() -> None:
    userNumber = int(input("number input: "))
    if (userNumber % 2) == 0:
        print("the number was even")
    else:
        print("the number was odd")


def main():
    evenOddChecker()

if __name__ == "__main__":
    main()