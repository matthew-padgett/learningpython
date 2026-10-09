def main():
    time = input("What time is it?: ")
    converted_time = convert(time)

    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")
    else:
        print("No meals during this time.")

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes)
    converted_minutes = minutes / 60
    converted_time = converted_minutes + int(hours)
    return converted_time


if __name__ == "__main__":
    main()