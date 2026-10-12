from operator import index


def main():
    camel_case = get_camel_case()
    convert_case_to_snake(camel_case)


def get_camel_case():
    camel_case = input("Type a variable name using camelCase!: ")

    # Takes the first letter and always lower cases it to ensure proper camel casing.
    if camel_case[0].isupper():
        first_character = camel_case[0].lower()
        rest_of_string = camel_case[1:]
        print(f"WARNING: I've adjust your improper camel case, \"{camel_case}\" to \"{"".join(first_character + rest_of_string)}\" which is a proper camel case!")
        camel_case = "".join(first_character + rest_of_string)
    return camel_case

def convert_case_to_snake(camel_case):
    snake_case = []
    for character in camel_case:
        if character.isupper():
            snake_case.append("_" + character) # appends " {character.isupper()}" to snake_case.
        else:
            snake_case.append(character)
    snake_case = "".join(snake_case).lower()
    print(snake_case)

if __name__ == "__main__":
    main()