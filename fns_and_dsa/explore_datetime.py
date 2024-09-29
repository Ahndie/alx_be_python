# explore_datetime.py

from datetime import datetime, timedelta  # Ensure correct imports

def display_current_datetime():
    """
    Displays the current date and time in '%Y-%m-%d %H:%M:%S' format.
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")  # Format the current time
    print(f"Current date and time: {formatted_time}")

    # Add 5 days to the current date
    future_time = current_time + timedelta(days=5)
    formatted_future_time = future_time.strftime("%Y-%m-%d %H:%M:%S")  # Format the future time
    print(f"Date and time after 5 days: {formatted_future_time}")

    # Subtract 10 hours from the current time
    past_time = current_time - timedelta(hours=10)
    formatted_past_time = past_time.strftime("%Y-%m-%d %H:%M:%S")  # Format the past time
    print(f"Date and time 10 hours ago: {formatted_past_time}")

    # Calculate the difference between two dates
    another_time = datetime(2024, 1, 1, 12, 0, 0)
    formatted_another_time = another_time.strftime("%Y-%m-%d %H:%M:%S")  # Format the specific time
    time_difference = another_time - current_time
    print(f"Time difference between {formatted_another_time} and now: {time_difference}")

def calculate_future_date(days: int):
    """
    Calculates the date that is a specified number of days from the current date, 
    and returns it in '%Y-%m-%d %H:%M:%S' format.
    
    Parameters:
    days (int): Number of days to add to the current date.

    Returns:
    str: The formatted future date as a string.
    """
    current_time = datetime.now()
    future_date = current_time + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")  # Return formatted date

# Call the functions
if __name__ == "__main__":
    display_current_datetime()

    # Example usage of calculate_future_date
    days_to_add = 10
    future_date = calculate_future_date(days_to_add)
    print(f"\nThe date {days_to_add} days from now will be: {future_date}")
