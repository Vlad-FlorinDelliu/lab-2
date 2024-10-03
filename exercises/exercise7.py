def checkWords() -> None:
    string1 = input("string 1: ")
    string2 = input("string 2: ")
    if string1.lower() == string2.lower():
        print("the two strings are the same")
    else:
        print("the two strings are not the same")

def main():
    checkWords()

if __name__ == "__main__":
    main()