def main():
    x, y = get_user_fraction()
    fuel_left = calculate_percentage(x, y)

    if fuel_left < 1:
        print("E")
    elif fuel_left == 100:
        print("F")
    else:
        print(f"{fuel_left:.0f}%")

def get_user_fraction():
    while True:
        fraction = input("Fraction: ")
        result = validate_user_fraction(fraction)
        if result is not None:
            return result

def validate_user_fraction(fraction):
    fraction = fraction.split("/")
    x = fraction[0]
    y = fraction[1]

    try:
        x = int(fraction[0])
    except ValueError:
        print(f"ERROR: x \"{x}\" is not a integer.")
        return None

    try:
        y = int(fraction[1])
    except ValueError:
        print(f"ERROR: y \"{y}\" is not an integer.")
        return None

    try:
        x / y
    except ZeroDivisionError:
        print(f"ERROR: The denominator must be greater than zero.")
        return None

    if x < 0 or x > y:
        print("ERROR: The numerator can't be negative or greater than the denominator.")
        return None

    return x, y


def calculate_percentage(x, y):
    percentage = (x / y) * 100
    return percentage

if __name__ == "__main__":
    main()