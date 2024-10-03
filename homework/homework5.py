def getStoppingDistance(speed:float, reactionTime:float, brakingDeceleration:float) -> float:
    return (speed * reactionTime) + ((speed**2) / (2 * brakingDeceleration))

def getStoppingDistanceData() -> float:
    speed = float(input("speed (km/h): "))
    speed = speed / 3.6
    reactionTime = float(input("reaction (s): "))
    brakingDeceleration = float(input("braking deceleration (m/s^2): "))
    return speed, reactionTime, brakingDeceleration

def showStoppingDistance() -> None:
    user_speed, user_reactionTime, user_brakingDeceleration = getStoppingDistanceData()
    user_stoppingDistance = getStoppingDistance(user_speed, user_reactionTime, user_brakingDeceleration)
    print(f"{user_stoppingDistance:.2f} meters")

def main():
    showStoppingDistance()

if __name__ == "__main__":
    main()