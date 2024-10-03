def translate_month_number_to_str(monthNumber: int) -> str:
    if monthNumber == 1:
        return "january"
    elif monthNumber == 2:
        return "february"
    elif monthNumber == 3:
        return "march"
    elif monthNumber == 4:
        return "april"
    elif monthNumber == 5:
        return "may"
    elif monthNumber == 6:
        return "june"
    elif monthNumber == 7:
        return "july"
    elif monthNumber == 8:
        return "august"
    elif monthNumber == 9:
        return "september"
    elif monthNumber == 10:
        return "october"
    elif monthNumber == 11:
        return "november"
    elif monthNumber == 12:
        return "december"
    else:
        return "invalid month number"

def getUserMonth() -> int:
    userMonth = int(input("user month input (1-12): "))
    return userMonth

def main():
    usermonth1 = getUserMonth()
    usermonth1String = translate_month_number_to_str(usermonth1)
    usermonth2 = getUserMonth()
    usermonth2String = translate_month_number_to_str(usermonth2)
    print(
        f"{usermonth1String}\n"
        f"{usermonth2String}"
    )

if __name__ == "__main__":
    main()