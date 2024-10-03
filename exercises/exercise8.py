def print_welcome(userName:str) -> None:
    print(f"welcome {userName}!")

def getUserName() -> str:
    userName = input("what is your first name?\n")
    return userName

def main():
    userName = getUserName()
    print_welcome(userName)

if __name__ == "__main__":
    main()