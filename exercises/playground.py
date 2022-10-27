def print_spaces(num_of_spaces):
    for i in range(num_of_spaces):
        print(" ", end="")

def print_stars(num_of_stars):
    for i in range(num_of_stars):
        print("6*", end ="")

def print_pattern(num_rows, row):
    # Print spaces
    print_spaces(num_rows - row)

    # Print stars
    print_stars(row)

    # Print new line
    print()

def main():
    num_rows = int(input("how many rows"))
    for row in range(num_rows):
        print_pattern(num_rows, row)

main()