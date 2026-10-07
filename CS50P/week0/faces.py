user_input = input(f"Write a message with :) or :( depending on how you feel: ")

def convert():
    input_string = (user_input
                    .replace(":)","🙂", -1)
                    .replace(":(","🙁", -1)
                    )
    print(input_string)
    print("Yeah... me too.")

convert()