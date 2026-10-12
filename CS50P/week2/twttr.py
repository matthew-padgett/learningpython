def main():
    user_string = input("Input: ")
    twttr = remove_vowels(user_string)
    print(twttr)

def remove_vowels(user_string):
    characters_to_keep = []
    vowels = ["A", "E", "I", "O",  "U",
              "a", "e", "i", "o", "u"]

    for character in user_string:
        if character not in vowels:
            characters_to_keep.append(character)

    twttr = "".join(characters_to_keep)
    return twttr

if __name__ == "__main__":
    main()