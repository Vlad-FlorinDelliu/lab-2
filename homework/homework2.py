def exclusive_to_include(paymentAmount:float, vatAmount:float) -> float:
    return paymentAmount * vatAmount

def getUserData() -> float:
    paymentAmount = float(input("amount excluding VAT: "))
    vatAmount = float(input("what is the VAT percentage: "))
    return paymentAmount, vatAmount

def vatCheckout() -> None:
    user_paymentAmount, user_vatAmount = getUserData()
    user_total = exclusive_to_include(user_paymentAmount, user_vatAmount)
    print(f"the amount you have to pay including VAT: {user_total:.2f}")

def main():
    vatCheckout()

if __name__ == "__main__":
    main()