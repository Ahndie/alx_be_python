# using for loop to generate a multiplication times table

number = int(input("Enter a number to see its multiplication table:"))
for i in range(1,11):
	result = number * i 
	print(f"{number} * {i} = {number * i}") 

