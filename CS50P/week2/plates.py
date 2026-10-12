def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if check_count(plate):
        if check_special_characters(plate):
            if check_first_two_are_letters(plate):
                if check_numbers_position(plate):
                    print("hello")

    else:
        print("False")


def check_count(plate):
    if len(plate) < 2:
        print("ERROR: Your plate does not meet the minimum amount of characters! Min: 2 Characters")
        return False
    elif len(plate) > 6:
        print("ERROR: Your plate exceeds the maximum amount of characters! Max: 6 Characters")
        return False
    else:
        return True

def check_special_characters(plate):
    for character in plate:
        if character.isalnum() is False:
            print("ERROR: Your plate contains special characters which are not allowed!")
            return False
    return True

def check_first_two_are_letters(plate):
    if not plate[:2].isalpha() and plate[:2].isascii():
        print("The first two characters of your plate must be letters!")
    return True

# Fix this
def check_numbers_position(plate):
    index = 2
    while index < len(plate) and plate[index].isdigit():
        index = index + 1
    return index == len(plate)

if __name__ == "__main__":
    main()