grocery_list = {}

while True:
    try:
        product = input().lower().strip()
    except EOFError:
        break

    if product in grocery_list:
        grocery_list[product] += 1
    else:
        grocery_list[product] = 1

for key, value in grocery_list.items():
    print(f"{value} {key.upper()}")