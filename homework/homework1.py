def getItemAmount() -> float:
    trouserPrice = 19.99
    tshirtPrice = 9.99
    vestPrice = 69.99
    trouserAmount = int(input("trouser amount: "))
    tshirtAmount = int(input("tshirt amount: "))
    vestAmount = int(input("vest amount: "))
    trouserPriceTotal = trouserAmount * trouserPrice
    tshirtPriceTotal = tshirtAmount * tshirtPrice
    vestPriceTotal = vestAmount * vestPrice
    return trouserPriceTotal, tshirtPriceTotal, vestPriceTotal

def checkout(trouserPriceTotal:float, tshirtPriceTotal:float, vestPriceTotal:float) -> float:
    return trouserPriceTotal + tshirtPriceTotal + vestPriceTotal

def main():
    user1_trouserPriceTotal, user1_tshirtPriceTotal, user1_vestPriceTotal = getItemAmount()
    user1_grandTotal = checkout(user1_trouserPriceTotal, user1_tshirtPriceTotal, user1_vestPriceTotal)
    #This print statement could be within the checkout function, if it was meant to be there. I understand that the checkout function has to return the value, and the the value had to be printed separately
    print(
        f"Total: {user1_grandTotal:.2f}"
    )
    


if __name__ == "__main__":
    main()