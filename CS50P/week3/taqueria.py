print("Please press ctrl + d to place your order.")
order = {}
prices = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

while True:
    try:
        item = input("Item: ").lower().strip()
    except EOFError:
        break

    if item not in prices:
        print("Item not on menu.")
        continue

    if item in order:
        order[item] += 1
    else:
        order[item] = 1

    total = 0
    for item in order:
        total += prices[item] * order[item]

    print(f"Total: ${total:.2f}")