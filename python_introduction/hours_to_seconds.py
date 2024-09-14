def convert_hours_to_seconds(hours):
    # Convert hours to seconds
    seconds = hours * 60 * 60
    return seconds

# Number of hours
hours = 2

# Convert hours to seconds
seconds = convert_hours_to_seconds(hours)

# Print the result in the specified format
print(f"{hours} hour(s) is {seconds} seconds.")
