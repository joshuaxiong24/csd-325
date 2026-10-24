# Joshua Xiong / 10/24/2026 / Module 1.3 Assignment

# The purpose of this code is to create a countdown of bottles of beer on the wall,
# starting from a user-defined number and counting down to zero. The program will
# print the lyrics of the song "99 Bottles of Beer" (or any number specified by the user)
# in a loop until there are no more bottles left.


def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(
            f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1

    # Special verse for 1 bottle
    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")


# Main program
num_bottles = int(input("How many bottles of beer are on the wall? "))

countdown(num_bottles)

print("Time to buy more bottles of beer!")
