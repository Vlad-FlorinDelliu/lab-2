def equationSolver(a:float, b:float, c:float = 0, d:float = 0) -> float:
    return ((a - b) + (c - d))

def main():
    number1 = equationSolver(1, 2, 3, 4)
    number2 = equationSolver(4, 3, 2, 1) #didn't understand "using the parameter names"
    number3 = equationSolver(1, 2)
    
    print(f"{number1} {number2} {number3}")

if __name__ == "__main__":
    main()