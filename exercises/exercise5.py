def checkPassingGrade() -> None:
    userScore = float(input("input score: "))
    if userScore >= 9.5:
        print("congrats, you pass!")
    else:
        print("you did not pass :<")


def main():
    checkPassingGrade()

if __name__ == "__main__":
    main()