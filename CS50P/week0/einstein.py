mass = int(
    input("Enter the mass here: ")
)

"E = MC^2"

speed_of_light = 300000000
energy = mass * (speed_of_light ** 2)
energy = f"{energy:,}"
print(f"E = ~{energy} Joules")