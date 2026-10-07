user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? "
                   .lower().strip()
                   )

if (user_input == 42
        or "forty-two"
        or "forty two"):
    print("Yes")
else:
    print("No")