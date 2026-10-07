
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d): # "$50.00" -> "50.00"
    dollars = d.strip("$")
    dollars = round(float(dollars), 1)
    return dollars

def percent_to_float(p): # "%15" -> "0.15"
    percent = p.strip("%")
    percent = float(percent)
    percent = percent / 100 # Converts 15 to 0.15
    return percent

main()