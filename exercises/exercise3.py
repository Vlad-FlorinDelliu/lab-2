
def checkUserLegalAge() -> None:
    userYearOfBirth = int(input("input year of birth: "))
    userMonthOfBirth = int(input("input month of birth: "))
    currentYear = 2024
    currentMonth = 10
    userAgeMonths = ((currentYear-userYearOfBirth) * 12) + (currentMonth - userMonthOfBirth)
    if userAgeMonths >= (12 * 18):
        print("you can drink alcohol in belgium")
    else:
        print("you can NOT drink alcohol in belgium")


def main():
   checkUserLegalAge() 

if __name__ == "__main__":
    main()