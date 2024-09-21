size = int(input("Enter the size of the pattern:" ))
   
# Ensure the user enters a positive integer
if size > 0:
    row = 0
    # Outer while loop for the rows
    while row < size:
    # Initialize column counter
    column = 0
        
    # Inner while loop for columns
    while column < size:
        print("*", end= " ")
        column += 1
         
    # Move to the next line after each row
    print()
    row += 1
