from datetime import datetime

def show_message(hour:int, firstName:str) -> str:
    if hour >= 7 and hour < 12:
        return f"good morning, {firstName}"
    if hour >=12 and hour < 13:
        return f"yay, it's afternoon, {firstName}"
    if hour >= 13 and hour < 17:
        return f"good afternoon, {firstName}"
    if hour >= 17 and hour < 21:
        return f"good evening, {firstName}"
    if hour >= 21 and hour < 7:
        return f"good night, {firstName}"

def show_welcome_message() -> None:
    hour = int(datetime.now().hour)
    firstName = input("what is your first name: ")
    welcome = show_message(hour, firstName)
    print(welcome)

def main():
    show_welcome_message()

if __name__ == "__main__":
    main()