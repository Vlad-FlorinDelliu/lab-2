def checkTwoNumbers() -> None:
    number1 = float(input("number 1: "))
    number2 = float(input("number 2: "))
    if number1 != number2:
        print("the numbers aren't the same")
    else:
        print("the numbers are the same!")

def main():
    checkTwoNumbers()

if __name__ == "__main__":
    main()