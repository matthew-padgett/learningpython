user_greeting = (input("Enter a greeting statement here: ")
                 .strip().lower())

if "hello" in user_greeting:
    print("$0")
elif user_greeting.startswith("h"):
    print("$20")
else:
    print("$100")