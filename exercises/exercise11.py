def show_max(number1:float, number2:float, number3:float) -> float:
    tempList = (number1, number2, number3)
    return max(tempList)

def main():
    maxNumber = show_max(3, 5, 2)
    print(maxNumber)

if __name__ == "__main__":
    main()