def give_celsius(t_in_fahrenheit:float) -> float:
    temp = (t_in_fahrenheit - 32) * (5 / 9)
    return temp

def give_fahrenheit(t_in_celsius:float) -> float:
    temp = (t_in_celsius * (9 / 5)) + 32
    return temp

def convertUserTemp(userUnit:str, userTemp:float) -> float:
    if userUnit.capitalize() == 'C':
        return (give_fahrenheit(userTemp))
    elif userUnit.capitalize() == 'F':
        return(give_celsius(userTemp))
    else:
        print("error")

def getUserUnit() -> str:
    userUnit = input("user unit (F - fahrenheit; C - celsius): ")
    return userUnit

def getUserTemp() -> float:
    userTemp = float(input("input temperature: "))
    return userTemp

def printUserConvertedTemp(userUnit:str, userConvertedTemp:float) -> None:
    if userUnit.capitalize() == 'C':
        print(f"converted temp: {userConvertedTemp:.2f} fahrenheit")
    elif userUnit.capitalize() == 'F':
        print(f"converted temp: {userConvertedTemp:.2f} celsius")
    else:
        print("error")

def main():
    userUnit1, userTemp1 = getUserUnit(), getUserTemp()
    userUnit2, userTemp2 = getUserUnit(), getUserTemp()
    user1_converted_temp = convertUserTemp(userUnit1, userTemp1)
    user2_converted_temp = convertUserTemp(userUnit2, userTemp2)
    printUserConvertedTemp(userUnit1, user1_converted_temp)
    printUserConvertedTemp(userUnit2, user2_converted_temp)

if __name__ == "__main__":
    main()