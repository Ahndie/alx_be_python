# explore_datetime.py

from datetime import datetime, timedelta  # Ensure correct imports

# Get the current date and time
current_time = datetime.now()
print(f"Current date and time: {current_time}")

# Add 5 days to the current date
future_time = current_time + timedelta(days=5)
print(f"Date and time after 5 days: {future_time}")

# Subtract 10 hours from the current time
past_time = current_time - timedelta(hours=10)
print(f"Date and time 10 hours ago: {past_time}")

# Calculate the difference between two dates
another_time = datetime(2024, 1, 1, 12, 0, 0)  # Fixed date and time
time_difference = another_time - current_time
print(f"Time difference between {another_time} and now: {time_difference}")
