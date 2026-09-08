import random
import argparse
import string
import secrets


special_characters = ["!", "@", "#", "$", "%", "_", "-"]
characters = string.ascii_letters + string.digits

parser = argparse.ArgumentParser (description='Password Generator using Python secrets.')

parser.add_argument(
    "length",
    type=int,
    help="Set the length of the password. "
)

parser.add_argument(
    "-spchar",
    action="store_true",
    help="Include special characters."
)

parser.add_argument(
    "-exclude",
    type=str,
    help="Exclude characters."
)

args = parser.parse_args()

if args.spchar:
    characters += "".join(special_characters)

filtered_characters = []

if args.exclude:
    for character in characters:
        if character not in args.exclude:
            filtered_characters.append(character)
    characters = "".join(filtered_characters)
else:
    pass

generated_password = "".join(secrets.choice(characters) for i in range(args.length))
print(generated_password)