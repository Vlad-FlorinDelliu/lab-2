def checkCaseSens() -> None:
    string1 = input("string 1: ")
    string2 = input("string 2: ")
    if string1 == string2:
        print("the two strings are the same")
    else:
        print("the two strings are not the same")


def main():
    checkCaseSens()

if __name__ == "__main__":
    main()