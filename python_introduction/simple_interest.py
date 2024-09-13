def calculate_simple_interest(principal, rate, time):

# Calculate the simple interest
    interest = principal * rate * time
    return interest

# Ensure that principal is set to 1000
principal = 1000   # Initial amount of money
rate = 0.05 # Interest rate (5%)
time = 3    # Time in years

# Calculate the interest
interest_earned = calculate_simple_interest(principal, rate, time)

# Print the interest in the desired format
print(f"The simple interest is: {interest_earned:.2f}")