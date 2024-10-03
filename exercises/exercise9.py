def create_welcome_in_class(userName:str, userClass:str = "1CTAI1") -> str:
    return f"welcome {userName} in {userClass}"

def getUserName() -> str:
    userName = input("what is your first name: ")
    return userName

def getUserClass() -> str:
    userClass = input("what is your class: ")
    return userClass

def main():
    userName = getUserName()
    userClass = getUserClass()
    print(create_welcome_in_class(userName, userClass))

if __name__ == "__main__":
    main()