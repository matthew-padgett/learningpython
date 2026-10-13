fruit_nutrition = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}
def main():
    user_input = input("Enter a fruit: ").lower().strip()

    for key in fruit_nutrition:
        if key == user_input:
            get_key_value(key)
            break
    else:
        print(f"ERROR: \"{user_input}\" is not found. Item is misspelled or isn't listed as fruit.")

def get_key_value(key):
    value = fruit_nutrition.get(key)
    print(f"Calories: {value}")

if __name__ == "__main__":
    main()


