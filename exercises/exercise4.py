def dogYearsToHumanYears() -> None:
    dogAge = int(input("dog age: "))
    if dogAge < 0:
        print("error")
    elif dogAge == 0:
        print("newborn pup")
    elif dogAge == 1:
        print("dog age = 14 human years")
    elif dogAge == 2:
        print("dog age = 22 human years")
    elif dogAge > 2:
        dogAge = 22 + ((dogAge - 2) * 5)
        print(f"dog age = {dogAge} human years")


def main():
    dogYearsToHumanYears()

if __name__ == "__main__":
    main()