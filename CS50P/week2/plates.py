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
                    return True
    return False

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
        return False
    return True

def check_numbers_position(plate):
    """
    This one was tough and I still don't fully understand what I wrote lol.

        v -- Start the index here, we already check if the first two are letters.
    0|1|2|3|4|5 # 6 Characters | len(plate) = 6
    A|A|#|#|#|#
        ^ -- Check current indexed character then move on.
    A|A|B|1|C|#
          ^-^ -- If digit after index is not a `.isdigit():` then is must be a letter.
    """
    index = 2

    # Skip any letters after the first two to find the first digit
    while index < len(plate) and plate[index].isalpha():
        index = index + 1

    # No digits at all, so nothing else to check
    if index == len(plate):
        return True

    # index now points at the first digit
    if plate[index] == "0":
        print("ERROR: A number can't start with 0!")
        return False

    # Every character from here on must be a digit
    while index < len(plate) and plate[index].isdigit():
        index = index + 1

    if index < len(plate):
        print("ERROR: Letters can't come after numbers!")
        return False

    return True

if __name__ == "__main__":
    main()
