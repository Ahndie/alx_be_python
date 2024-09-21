# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Ensure the user enters a positive integer
if size > 0:
    # Outer loop for the rows
    for i in range(size):
        # Inner loop for the columns
        for j in range(size):
            print("*", end=" ")
        # Move to the next line after each row
        print()
else:
    print("Please enter a positive integer.")


