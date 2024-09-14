def calculate_future_age(user_age, years_added):

	#Calculate future age in 2050
	future_age = user_age + years_added
	return future_age 

# Prompt the user for their age
user_age = int(input("How old are you? "))

# Calculate the future age by adding 27 to current age
age_in_2050 = calculate_future_age(user_age, 27)

# Prints result in the specified format
print(f"In 2050, you will be {age_in_2050} years old.")
