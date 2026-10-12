def main():
  amount_due = 50
  payment(amount_due)

def payment(amount_due):
    acceptable_denominations = [25, 10, 5]
    change = 0

    while amount_due > 0:
        print(f"Amount due: {amount_due}¢")
        coin = int(input("Insert coin: "))

        if coin in acceptable_denominations:
            amount_due = amount_due - coin
        else:
            print("--- Coin is not an acceptable denomination. Please insert, 25¢, 10¢, 5¢ ---")

    # Gives the user their change.
    if amount_due < 0:
        change = amount_due * -1
    purchase_complete(change)

def purchase_complete(change):
    print("--- Purchase Complete ---")
    if change > 0:
        print(f"Your change is: {change}¢")
    print("Enjoy your coke!")


if __name__ == "__main__":
    main()